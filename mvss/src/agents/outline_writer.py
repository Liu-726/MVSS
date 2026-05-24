import os
import numpy as np
import tiktoken # 如果您没用到tiktoken可以注释掉，或者确保已安装
from tqdm import trange, tqdm
import time
import re
from src.model import APIModel
from src.database import database
from src.utils import tokenCounter
from src.prompt import ROUGH_OUTLINE_PROMPT, MERGING_OUTLINE_PROMPT, SUBSECTION_OUTLINE_PROMPT, EDIT_FINAL_OUTLINE_PROMPT

class outlineWriter():
    
    def __init__(self, model:str, api_key:str, api_url:str, database) -> None:
        
        self.model, self.api_key, self.api_url = model, api_key, api_url 
        self.api_model = APIModel(self.model, self.api_key, self.api_url)

        self.db = database
        self.token_counter = tokenCounter()
        self.input_token_usage, self.output_token_usage = 0, 0

    def draft_outline(self, topic, reference_num = 600, chunk_size = 30000, section_num = 6, prior_md_content="", prior_json_content=""):
        # Get database
        references_ids = self.db.get_ids_from_query(topic, num = reference_num, shuffle = True)
        references_infos = self.db.get_paper_info_from_ids(references_ids)

        references_titles = [r['title'] for r in references_infos]
        references_abs = [r['abs'] for r in references_infos]
        
        if not references_abs:
            print("Warning: No references found. Generating outline based on topic only.")
            abs_chunks, titles_chunks = [[""]], [[""]]
        else:
            abs_chunks, titles_chunks = self.chunking(references_abs, references_titles, chunk_size=chunk_size)

        # generate rough section-level outline
        outlines = self.generate_rough_outlines(
            topic=topic, 
            papers_chunks = abs_chunks, 
            titles_chunks = titles_chunks, 
            section_num=section_num,
            prior_md_content=prior_md_content,
            prior_json_content=prior_json_content
        )
        
        # merge outline
        section_outline = self.merge_outlines(topic=topic, outlines=outlines)

        # generate subsection-level outline
        subsection_outlines = self.generate_subsection_outlines(
            topic=topic, 
            section_outline= section_outline,
            rag_num= 50,
            prior_md_content=prior_md_content,
            prior_json_content=prior_json_content
        )
        
        merged_outline = self.process_outlines(section_outline, subsection_outlines)
        
        # edit final outline
        final_outline = self.edit_final_outline(merged_outline)

        return final_outline

    def compute_price(self):
        return self.token_counter.compute_price(input_tokens=self.input_token_usage, output_tokens=self.output_token_usage, model=self.model)

    def generate_rough_outlines(self, topic, papers_chunks, titles_chunks, section_num = 8, prior_md_content="", prior_json_content=""):
        prompts = []
        if not papers_chunks: papers_chunks = [[]]
        if not titles_chunks: titles_chunks = [[]]

        for i in trange(len(papers_chunks)):
            titles = titles_chunks[i]
            papers = papers_chunks[i]
            paper_texts = '' 
            for t, p in zip(titles, papers):
                paper_texts += f'---\npaper_title: {t}\n\npaper_content:\n\n{p}\n'
            paper_texts+='---\n'

            prompt = self.__generate_prompt(ROUGH_OUTLINE_PROMPT, paras={
                'PAPER LIST': paper_texts, 
                'TOPIC': topic, 
                'SECTION NUM': str(section_num),
                'PRIOR KNOWLEDGE MD': prior_md_content,
                'PRIOR KNOWLEDGE JSON': prior_json_content
            })
            prompts.append(prompt)
        
        self.input_token_usage += self.token_counter.num_tokens_from_list_string(prompts)
        outlines = self.api_model.batch_chat(text_batch=prompts, temperature=1)
        self.output_token_usage += self.token_counter.num_tokens_from_list_string(outlines)
        return outlines
    
    def merge_outlines(self, topic, outlines):
        outline_texts = '' 
        for i, o in enumerate(outlines):
            outline_texts += f'---\noutline_id: {i}\n\noutline_content:\n\n{o}\n'
        outline_texts+='---\n'
        
        prompt = self.__generate_prompt(MERGING_OUTLINE_PROMPT, paras={'OUTLINE LIST': outline_texts, 'TOPIC':topic})
        self.input_token_usage += self.token_counter.num_tokens_from_string(prompt)

        outline = self.api_model.chat(prompt, temperature=1)
        outline = outline.replace('```json', '').replace('```', '').strip()
        
        self.output_token_usage += self.token_counter.num_tokens_from_string(outline)
        return outline
    
    def generate_subsection_outlines(self, topic, section_outline, rag_num, prior_md_content="", prior_json_content=""):
        survey_title, survey_sections, survey_section_descriptions = self.extract_title_sections_descriptions(section_outline)

        if not survey_sections:
            print("Warning: Failed to parse sections from merged outline. Using fallback.")
            survey_sections = ["Introduction", "Methodology", "Conclusion"]
            survey_section_descriptions = ["Overview", "Methods", "Summary"]

        prompts = []
        for section_name, section_description in zip(survey_sections, survey_section_descriptions):
            references_ids = self.db.get_ids_from_query(section_description, num = rag_num, shuffle = True)
            references_infos = self.db.get_paper_info_from_ids(references_ids)

            references_titles = [r['title'] for r in references_infos]
            references_papers = [r['abs'] for r in references_infos]
            paper_texts = '' 
            for t, p in zip(references_titles, references_papers):
                paper_texts += f'---\npaper_title: {t}\n\npaper_content:\n\n{p}\n'
            paper_texts+='---\n'
            
            prompt = self.__generate_prompt(SUBSECTION_OUTLINE_PROMPT, paras={
                'OVERALL OUTLINE': section_outline,
                'SECTION NAME': section_name,
                'SECTION DESCRIPTION':section_description,
                'TOPIC':topic,
                'PAPER LIST':paper_texts,
                'PRIOR KNOWLEDGE MD': prior_md_content,
                'PRIOR KNOWLEDGE JSON': prior_json_content
            })
            prompts.append(prompt)
        
        self.input_token_usage += self.token_counter.num_tokens_from_list_string(prompts)
        sub_outlines = self.api_model.batch_chat(prompts, temperature=1)
        self.output_token_usage += self.token_counter.num_tokens_from_list_string(sub_outlines)
        
        return sub_outlines

    def edit_final_outline(self, outline):
        prompt = self.__generate_prompt(EDIT_FINAL_OUTLINE_PROMPT, paras={'OVERALL OUTLINE': outline})
        self.input_token_usage += self.token_counter.num_tokens_from_string(prompt)
        outline = self.api_model.chat(prompt, temperature=1)
        self.output_token_usage += self.token_counter.num_tokens_from_string(outline)
        return outline.replace('<format>\n','').replace('</format>','')
 
    def __generate_prompt(self, template, paras):
        prompt = template
        for k in paras.keys():
            prompt = prompt.replace(f'[{k}]', paras[k])
        return prompt
    
    def extract_title_sections_descriptions(self, outline):
        title_match = re.search(r'(?:^|\n)(?:#|\*\*|)?\s*Title\s*(?:\*\*|)?\s*[:.]?\s*(.*)', outline, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
        else:
            lines = [l.strip() for l in outline.split('\n') if l.strip()]
            title = lines[0] if lines else "Survey Title"

        sections, descriptions = [], []
        lines = outline.split('\n')
        
        sec_pattern = re.compile(r'(?:^|\n)(?:#|\*\*|)?\s*Section\s*\d+\s*(?:\*\*|)?\s*[:.]\s*(.*)', re.IGNORECASE)
        desc_pattern = re.compile(r'(?:^|\n)(?:#|\*\*|)?\s*Description\s*(?:\d+)?\s*(?:\*\*|)?\s*[:.]\s*(.*)', re.IGNORECASE)

        current_sec_idx = -1

        for i, line in enumerate(lines):
            line = line.strip()
            if not line: continue

            sec_match = sec_pattern.match(line)
            if sec_match:
                sections.append(sec_match.group(1).strip())
                descriptions.append("")
                current_sec_idx += 1
                
                for lookahead in range(1, 6):
                    if i + lookahead < len(lines):
                        next_line = lines[i + lookahead].strip()
                        desc_match = desc_pattern.match(next_line)
                        if desc_match:
                            descriptions[current_sec_idx] = desc_match.group(1).strip()
                            break
                        if sec_pattern.match(next_line) or next_line.startswith('#'):
                            break
                continue

        if not sections:
            for line in lines:
                if line.strip().startswith("## "):
                    sections.append(line.strip().replace("##", "").strip())
                    descriptions.append("Detailed discussion on this topic.")

        return title, sections, descriptions
    
    def extract_subsections_subdescriptions(self, outline):
        subsections, subdescriptions = [], []
        lines = outline.split('\n')
        
        sub_pattern = re.compile(r'(?:^|\n)(?:#|\*\*|)?\s*Subsection\s*[\d.]+\s*(?:\*\*|)?\s*[:.]\s*(.*)', re.IGNORECASE)
        desc_pattern = re.compile(r'(?:^|\n)(?:#|\*\*|)?\s*Description\s*(?:[\d.]+)?\s*(?:\*\*|)?\s*[:.]\s*(.*)', re.IGNORECASE)

        current_sub_idx = -1

        for i, line in enumerate(lines):
            line = line.strip()
            
            sub_match = sub_pattern.match(line)
            if sub_match:
                subsections.append(sub_match.group(1).strip())
                subdescriptions.append("")
                current_sub_idx += 1
                
                for lookahead in range(1, 6):
                    if i + lookahead < len(lines):
                        next_line = lines[i + lookahead].strip()
                        desc_match = desc_pattern.match(next_line)
                        if desc_match:
                            subdescriptions[current_sub_idx] = desc_match.group(1).strip()
                            break
                        if sub_pattern.match(next_line) or next_line.startswith('#'):
                            break

        if not subsections:
            for line in lines:
                if line.strip().startswith("### "):
                    subsections.append(line.strip().replace("###", "").strip())
                    subdescriptions.append("Detailed analysis.")

        return subsections, subdescriptions
    
    def chunking(self, papers, titles, chunk_size = 14000):
        paper_chunks, title_chunks = [], []
        if not papers:
            return [[]], [[]]

        total_length = self.token_counter.num_tokens_from_list_string(papers)
        if chunk_size <= 0: chunk_size = 14000
        if total_length == 0: total_length = 1
        
        num_of_chunks = int(total_length / chunk_size) + 1
        avg_len = int(total_length / num_of_chunks) + 1
        
        split_points = []
        l = 0
        for j in range(len(papers)):
            l += self.token_counter.num_tokens_from_string(papers[j])
            if l > avg_len:
                l = 0
                split_points.append(j)
                continue
        start = 0
        for point in split_points:
            paper_chunks.append(papers[start:point])
            title_chunks.append(titles[start:point])
            start = point
        paper_chunks.append(papers[start:])
        title_chunks.append(titles[start:])
        return paper_chunks, title_chunks
        
    def process_outlines(self, section_outline, sub_outlines):
        res = ''
        survey_title, survey_sections, survey_section_descriptions = self.extract_title_sections_descriptions(section_outline)
        res += f'# {survey_title}\n\n'
        
        limit = min(len(survey_sections), len(sub_outlines))
        
        for i in range(limit):
            section = survey_sections[i]
            desc = survey_section_descriptions[i] if i < len(survey_section_descriptions) else ""
            
            res += f'## {i+1} {section}\nDescription: {desc}\n\n'
            
            subsections, subsection_descriptions = self.extract_subsections_subdescriptions(sub_outlines[i])
            for j in range(len(subsections)):
                sub = subsections[j]
                sub_desc = subsection_descriptions[j] if j < len(subsection_descriptions) else ""
                res += f'### {i+1}.{j+1} {sub}\nDescription: {sub_desc}\n\n'
        return res