import os
import re
import threading
import numpy as np
from tqdm import tqdm
import time
import copy
from src.model import APIModel
from src.utils import tokenCounter
from src.prompt import SUBSECTION_WRITING_PROMPT, CHECK_CITATION_PROMPT, LOCAL_TABLE_REFLECT_PROMPT

class subsectionWriter():
    
    def __init__(self, model:str, api_key:str, api_url:str,  database) -> None:
        self.model, self.api_key, self.api_url = model, api_key, api_url
        self.api_model = APIModel(self.model, self.api_key, self.api_url)
        self.db = database
        self.token_counter = tokenCounter()
        self.input_token_usage, self.output_token_usage = 0, 0

    def clean_ai_text(self, text, subsection_name):
        if not text: return ""
        
        text = text.strip()
        lines = text.split('\n')
        
        if len(lines) > 0 and lines[0].strip().startswith('```'):
            lines = lines[1:]
        
        if len(lines) > 0 and lines[-1].strip() == '```':
            lines = lines[:-1]
            
        text = '\n'.join(lines).strip()

        pattern = r'^(?:#+\s*)?' + re.escape(subsection_name) + r'.*\n*'
        text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.MULTILINE).strip()
        
        text = re.sub(r'^\s*[-*_]{3,}\s*$', '', text, flags=re.MULTILINE).strip()

        lines = text.split('\n')
        if lines and lines[0].strip().startswith('#'):
            text = '\n'.join(lines[1:]).strip()
            
        return text

    def clean_table_text(self, text):
        if not text: return ""
        
        text = text.replace("```markdown", "").replace("```", "").strip()

        lines = text.split('\n')
        valid_lines = []
        
        for line in lines:
            line = line.strip()
            if not line: continue
            
            if "|" in line:
                valid_lines.append(line)
        
        if len(valid_lines) < 2:
            return ""

        text = "\n".join(valid_lines)

        text = re.sub(r'\]\(.*?\)', ']', text)
        
        return text.strip()

    def preprocess_prior_content(self, raw_text):
        if not raw_text: return ""
        parts = re.split(r'\nReferences\n|\nReference\n', raw_text, flags=re.IGNORECASE)
        if len(parts) < 2: return raw_text.strip()
        
        tree_body, ref_list = parts[0], parts[1]
        id_to_title = {}
        ref_pattern = re.compile(r'\[(\d+)\]\s*.*?\((?:.*?)\)\.\s*(.*?)(?:\.\s*arXiv|\.$|$)', re.DOTALL | re.MULTILINE)
        
        chunks = re.split(r'(?=\[\d+\])', ref_list)
        for chunk in chunks:
            if not chunk.strip(): continue
            match = ref_pattern.search(chunk)
            if match:
                rid, title = match.group(1), match.group(2).replace('\n', ' ').strip()
                if title.endswith('.'): title = title[:-1]
                id_to_title[rid] = title

        def replacer(m):
            return f"[{id_to_title[m.group(1)]}]" if m.group(1) in id_to_title else m.group(0)

        return re.sub(r'\[(\d+)\]', replacer, tree_body).strip()

    def write(self, topic, outline, rag_num=30, subsection_len=500, refining=True, reflection=True, prior_md_content="", prior_json_content=""):
        parsed = self.parse_outline(outline)
        sections_len = len(parsed['sections'])
        if sections_len == 0:
            print("Error: Outline parsing failed.")
            return "", "", {}

        print("--> Retrieving papers...")
        section_paper_texts = [[] for _ in range(sections_len)]
        for i in tqdm(range(sections_len)):
            if i < len(parsed['subsection_descriptions']):
                descriptions = parsed['subsection_descriptions'][i]
                for desc in descriptions:
                    ids = self.db.get_ids_from_query(desc, num=rag_num)
                    infos = self.db.get_paper_info_from_ids(ids)
                    text_block = ""
                    for info in infos:
                        text_block += f"---\npaper_title: {info['title']}\npaper_content:\n{info['abs']}\n---\n"
                    section_paper_texts[i].append(text_block)

        processed_tree = self.preprocess_prior_content(prior_md_content)

        print("--> Writing content...")
        section_contents = [[] for _ in range(sections_len)]
        threads = []
        for i in range(sections_len):
            t = threading.Thread(target=self.write_subsection_task, args=(
                section_paper_texts[i], topic, outline, 
                parsed['sections'][i], parsed['subsections'][i], parsed['subsection_descriptions'][i], 
                section_contents, i, subsection_len, prior_md_content
            ))
            threads.append(t)
            t.start()
            time.sleep(0.5) 
        
        for t in threads: t.join()

        print("--> Assembling document...")
        raw_survey = self.generate_document(parsed, section_contents, processed_tree)
        
        raw_survey_with_references, raw_references = self.process_references(raw_survey)

        return raw_survey+'\n', raw_survey_with_references+'\n', raw_references

    def write_subsection_task(self, paper_texts_l, topic, outline, section, subsections, subdescriptions, res_container, idx, sub_len, prior_md):
        final_texts = []
        prompts = []
        
        for j in range(len(subsections)):
            desc = subdescriptions[j] if j < len(subdescriptions) else ""
            p_text = paper_texts_l[j] if j < len(paper_texts_l) else ""
            
            p = SUBSECTION_WRITING_PROMPT.replace('[TOPIC]', topic)\
                .replace('[OVERALL OUTLINE]', outline)\
                .replace('[PAPER_LIST]', p_text)\
                .replace('[PRIOR KNOWLEDGE MD]', prior_md)\
                .replace('[SUBSECTION NAME]', subsections[j])\
                .replace('[SECTION NAME]', section)\
                .replace('[DESCRIPTION]', desc)\
                .replace('[WORD NUM]', str(sub_len))
            prompts.append(p)
        
        drafts = self.api_model.batch_chat(prompts, temperature=1)
        drafts = [d.replace('<format>', '').replace('</format>', '') for d in drafts]

        for j, (draft, sub_name) in enumerate(zip(drafts, subsections)):
            p_text = paper_texts_l[j] if j < len(paper_texts_l) else ""
            
            clean_draft = self.clean_ai_text(draft, sub_name)

            check_p = CHECK_CITATION_PROMPT.replace('[SUBSECTION]', clean_draft).replace('[TOPIC]', topic).replace('[PAPER LIST]', p_text)
            checked_text = self.api_model.chat(check_p, temperature=1).replace('<format>', '').replace('</format>', '')
            
            checked_text = self.clean_ai_text(checked_text, sub_name)

            table_p = LOCAL_TABLE_REFLECT_PROMPT.replace('[SUBSECTION_CONTENT]', checked_text)\
                                                .replace('[PAPER_LIST]', p_text)
            table_res = self.api_model.chat(table_p, temperature=0.1) 
            
            if "NO_TABLE" not in table_res:
                clean_table = self.clean_table_text(table_res)
                if len(clean_table) > 20: 
                    checked_text += f"\n\n**Table: Comparison of approaches in {sub_name}**\n\n{clean_table}\n"
            
            final_texts.append(checked_text)
        
        res_container[idx] = final_texts

    def generate_document(self, parsed_outline, subsection_contents, prior_md_content=""):
        document = []
        document.append(f"# {parsed_outline['title']}\n")
        
        for i, section in enumerate(parsed_outline['sections']):
            document.append(f"## {section}\n")
            
            if i < len(parsed_outline['section_descriptions']):
                desc = parsed_outline['section_descriptions'][i]
                if desc and len(desc) > 5:
                    document.append(f"{desc}\n")

            if i < len(parsed_outline['subsections']):
                for j, subsection in enumerate(parsed_outline['subsections'][i]):
                    document.append(f"### {subsection}\n")
                    if i < len(subsection_contents) and j < len(subsection_contents[i]):
                        document.append(subsection_contents[i][j] + "\n")
            
            if i == 0 and prior_md_content:
                document.append("\n### Roadmap and Taxonomy\n")
                document.append("The following taxonomy tree outlines the structure of this survey:\n\n")
                document.append(prior_md_content + "\n\n")
        
        return "\n".join(document)

    def process_references(self, text):
        raw_citations_iter = re.finditer(r'\[(.*?)\]', text)
        
        citations_in_order = []
        for match in raw_citations_iter:
            content = match.group(1)
            if content.strip().isdigit(): continue 
            
            clean_content = re.sub(r'\(.*?\)', '', content).strip()
            parts = [p.strip() for p in clean_content.split(';') if p.strip()]
            citations_in_order.extend(parts)

        if not citations_in_order: return text, {}

        unique_titles_query = list(set(citations_in_order))
        ids = self.db.get_titles_from_citations(unique_titles_query)
        
        citation_to_db_id = {cit: pid for cit, pid in zip(unique_titles_query, ids)}
        valid_db_infos = self.db.get_paper_info_from_ids(ids)
        db_id_to_real_title = {p['id']: p['title'] for p in valid_db_infos}
        
        input_title_to_real_title = {}
        for cit in unique_titles_query:
            if cit in citation_to_db_id:
                did = citation_to_db_id[cit]
                if did in db_id_to_real_title:
                    input_title_to_real_title[cit] = db_id_to_real_title[did]

        title_to_num = {}            
        final_refs_id_map = {}       
        final_refs_title_map = {}    
        current_num = 1

        for cit in citations_in_order:
            if cit not in input_title_to_real_title:
                continue

            real_title = input_title_to_real_title[cit]
            arxiv_id = citation_to_db_id.get(cit) 

            if real_title not in title_to_num:
                title_to_num[real_title] = current_num

                final_refs_id_map[current_num] = arxiv_id if arxiv_id else real_title

                final_refs_title_map[current_num] = real_title

                current_num += 1
            
        def replacer(m):
            content = m.group(1)
            if content.strip().isdigit(): return m.group(0)

            clean_content = re.sub(r'\(.*?\)', '', content).strip()
            parts = [p.strip() for p in clean_content.split(';')]

            nums = []
            for p in parts:
                if p in input_title_to_real_title:
                    real_t = input_title_to_real_title[p]
                    if real_t in title_to_num:
                        nums.append(str(title_to_num[real_t]))

            if not nums: return m.group(0)
            return f"[{', '.join(nums)}]"

        final_text = re.sub(r'\[(.*?)\]', replacer, text)

        ref_str = "\n\n## References\n"
        for n in sorted(final_refs_title_map.keys()):
            t_clean = final_refs_title_map[n].replace('\n', ' ')
            ref_str += f"[{n}] {t_clean}\n\n"

        return final_text + ref_str, final_refs_id_map

    def parse_outline(self, outline):
        result = {"title": "", "sections": [], "section_descriptions": [], "subsections": [], "subsection_descriptions": []}
        lines = outline.split('\n')
        current_section_index = -1
        
        for line in lines:
            line = line.strip()
            if line.startswith("# ") and not result["title"]:
                result["title"] = line[2:].strip()
            elif line.lower().startswith("title:") and not result["title"]:
                result["title"] = line.split(":", 1)[1].strip()

        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith("## "):
                section_title = line[3:].strip()
                result["sections"].append(section_title)
                result["subsections"].append([])
                result["subsection_descriptions"].append([])
                result["section_descriptions"].append("") 
                current_section_index += 1
                for lookahead in range(1, 5):
                    if i + lookahead < len(lines):
                        next_line = lines[i + lookahead].strip()
                        if next_line.lower().startswith("description"):
                            desc = next_line.split(":", 1)[1].strip() if ":" in next_line else next_line
                            result["section_descriptions"][current_section_index] = desc
                            break
                        if next_line.startswith("#"): break
            elif line.startswith("### "):
                if current_section_index >= 0:
                    subsection_title = line[4:].strip()
                    result["subsections"][current_section_index].append(subsection_title)
                    result["subsection_descriptions"][current_section_index].append("")
                    for lookahead in range(1, 5):
                        if i + lookahead < len(lines):
                            next_line = lines[i + lookahead].strip()
                            if next_line.lower().startswith("description"):
                                desc = next_line.split(":", 1)[1].strip() if ":" in next_line else next_line
                                result["subsection_descriptions"][current_section_index][-1] = desc
                                break
                            if next_line.startswith("#"): break
        if not result["title"]: result["title"] = "Survey"
        return result

    def compute_price(self): return self.token_counter.compute_price(input_tokens=self.input_token_usage, output_tokens=self.output_token_usage, model=self.model)
    def extract_citations(self, markdown_text):
        pattern = re.compile(r'\[(.*?)\]')
        matches = pattern.findall(markdown_text)
        citations = list()
        for match in matches:
            parts = match.split(';')
            for part in parts:
                cit = part.strip()
                if cit not in citations: citations.append(cit)
        return citations
    def refine_subsections(self, topic, outline, section_content): return section_content 
    def lce(self, topic, outline, contents, res_l, idx): pass
    def extract_title_sections_descriptions(self, outline): return self.parse_outline(outline)["title"], [], []
    def extract_subsections_subdescriptions(self, outline): return [], []