

import os
import re
import threading
import time
import json
from typing import List, Dict, Any
from tqdm import tqdm
from src.model import APIModel
from src.utils import tokenCounter
from src.database import database
from src.prompt import TREE_PROMPT


class TreeWriter():
    def __init__(self, model: str, api_key: str, api_url: str, db: database) -> None:
        self.model, self.api_key, self.api_url = model, api_key, api_url
        self.api_model = APIModel(self.model, self.api_key, self.api_url)
        self.db = db
        self.token_counter = tokenCounter()
        self.input_token_usage, self.output_token_usage = 0, 0

    # ------------------------
    # Public entry
    # ------------------------
    def write_tree(self, topic: str, outline: str, rag_num: int = 30):
        """
        Main pipeline:
        1) Parse outline
        2) Retrieve references
        3) Build per-subsection paper texts
        4) Parallel generate section tree snippets
        5) Integrate all sections into a single Markdown tree
        6) Post-process: renumber citations and build References; return JSON form
        """
        if not isinstance(outline, str) or not outline.strip():
            raise ValueError("write_tree: 'outline' must be a non-empty string")

        parsed_outline = self.parse_outline(outline)
        self._validate_parsed_outline(parsed_outline)

        # Prepare containers
        section_count = len(parsed_outline['sections'])
        section_paper_texts: List[List[str]] = [[] for _ in range(section_count)]
        total_ids: List[str] = []
        section_references_ids: List[List[List[str]]] = [[] for _ in range(section_count)]

        # 1) Retrieve references per subsection description
        for i, descriptions in enumerate(parsed_outline['subsection_descriptions']):
            for d in descriptions:
                q = d if isinstance(d, str) else ("" if d is None else str(d))
                refs = self.db.get_ids_from_query(q, num=rag_num, shuffle=False)
                total_ids += refs
                section_references_ids[i].append(refs)

        # 2) Fetch paper metadata
        unique_ids = list(set(total_ids))
        total_refs_info = self.db.get_paper_info_from_ids(unique_ids)
        temp_title_dic = {p['id']: (p.get('title') or "") for p in total_refs_info}
        temp_abs_dic = {p['id']: (p.get('abs') or "") for p in total_refs_info}

        # 3) Build the raw text bundle per subsection within each section
        for i, section_subrefs in enumerate(section_references_ids):
            for refs_ids in section_subrefs:
                paper_texts = ""
                for pid in refs_ids:
                    paper_texts += (
                        f"---\n\nref_id: {pid}\n"
                        f"paper_title: {temp_title_dic.get(pid, '')}\n\n"
                        f"paper_content:\n{temp_abs_dic.get(pid, '')}\n"
                    )
                paper_texts += "---\n"
                section_paper_texts[i].append(paper_texts)

        # 4) Generate section trees in parallel
        section_content: List[List[str]] = [[] for _ in range(section_count)]
        threads = []
        for i in range(section_count):
            t = threading.Thread(
                target=self._write_section_tree,
                args=(
                    section_paper_texts[i],
                    topic,
                    outline,
                    parsed_outline['sections'][i],
                    parsed_outline['subsections'][i],
                    parsed_outline['subsection_descriptions'][i],
                    section_content,
                    i,
                    total_refs_info
                ),
                daemon=True
            )
            threads.append(t)
            t.start()
            time.sleep(0.05)
        for t in threads:
            t.join()

        # Flatten section snippets; ensure strings
        flat_snippets = []
        for seg in section_content:
            for s in seg:
                if not isinstance(s, str):
                    s = "" if s is None else str(s)
                flat_snippets.append(s)
        all_section_texts = "\n".join(flat_snippets)

        # Build paper list string
        paper_list_str = "\n".join([
            f"{p.get('id','')}: {p.get('title','')} ({p.get('year','n.d.')})"
            for p in total_refs_info
        ])

        # 5) Integrate all sections into a unified tree
        integrate_prompt = (
            "You are given multiple tree sections as Markdown:\n"
            f"{all_section_texts}\n"
            "PAPER LIST\n"
            f"{paper_list_str}\n"
            "Please integrate them into a single unified tree in Markdown format.\n"
            "Very Important:\n"
            '- The tree must strictly follow the indentation rule.\n'
            '- Each level of depth is represented by exactly "|     " (vertical bar + 5 spaces).\n'
            '- Each branch must start with "|----".\n'
            '- The spacing and alignment must remain consistent across the whole tree.\n'
            '- Use only the [RID:xxxx] format for citations.\n'
            '- Only use IDs provided in PAPER LIST. Do NOT invent or guess new IDs.\n'
            '- Actively distribute citations across as many different IDs as possible.\n'
            '- Avoid excessive repetition of the same RID; reuse only if strictly relevant.\n'
            "Return only the final tree diagram in Markdown.\n"
        )

        unified_tree_md = self.api_model.chat(integrate_prompt, temperature=1)
        if not isinstance(unified_tree_md, str):
            # Retry once if None or non-string is returned
            unified_tree_md = "" if unified_tree_md is None else str(unified_tree_md)
        unified_tree_md = unified_tree_md.replace('<format>', '').replace('</format>', '')

        if not unified_tree_md.strip():
            # Retry once with a slightly simpler prompt (fallback)
            fallback_prompt = (
                f"{all_section_texts}\n\n"
                "Integrate the above into ONE Markdown tree. "
                "Use only [RID:xxxx] from the given section texts. "
                "Return ONLY the tree."
            )
            retry_md = self.api_model.chat(fallback_prompt, temperature=1)
            if not isinstance(retry_md, str):
                retry_md = "" if retry_md is None else str(retry_md)
            retry_md = retry_md.replace('<format>', '').replace('</format>', '')
            if retry_md.strip():
                unified_tree_md = retry_md
            else:
                raise RuntimeError("Integration model returned empty content after retry.")

        # 6) Post-processing
        rid_order = self.extract_rids_from_tree(unified_tree_md.splitlines())
        final_tree = self.renumber_and_build_refs(unified_tree_md, rid_order)
        tree_json = self.convert_tree_md_to_json(final_tree.splitlines())
        return final_tree, tree_json, rid_order

    # ------------------------
    # Thread worker
    # ------------------------
    def _write_section_tree(
        self,
        paper_texts_l: List[str],
        topic: str,
        outline: str,
        section: str,
        subsections: List[str],
        subdescriptions: List[str],
        res_l: List[List[str]],
        idx: int,
        total_refs_info: List[Dict[str, Any]]
    ):
        """
        Build prompts per subsection and call batch_chat.
        Robust to None returns, length mismatch, and exceptions.
        """
        try:
            paper_list_str = "\n".join([
                f"{p.get('id','')}: {p.get('title','')} ({p.get('year','n.d.')})"
                for p in total_refs_info
            ])

            prompts = []
            # Align lengths robustly
            pair_count = min(len(subsections), len(subdescriptions))
            for j in range(pair_count):
                sub = subsections[j] if isinstance(subsections[j], str) else str(subsections[j] or "")
                desc = subdescriptions[j] if isinstance(subdescriptions[j], str) else str(subdescriptions[j] or "")
                paper_texts = paper_texts_l[j] if j < len(paper_texts_l) else ""

                paras = {
                    "TOPIC": topic or "",
                    "SECTION NAME": section or "",
                    "SUBSECTION NAME": sub,
                    "DESCRIPTION": desc,
                    "PAPER LIST": paper_list_str,
                    "OVERALL OUTLINE": outline or "",
                    "PAPER TEXTS": paper_texts or ""
                }
                prompt = self.__generate_prompt(TREE_PROMPT, paras)
                prompt += (
                    "\n\nImportant: "
                    "ONLY cite using [RID:xxxx] where xxxx is exactly from PAPER LIST above. "
                    "Do NOT make up IDs. "
                    "Distribute citations across as many different IDs as possible. "
                    "For each keyword, try to include 3 different [RID] values whenever relevant."
                )
                prompts.append(prompt)

            self.input_token_usage += self.token_counter.num_tokens_from_list_string(prompts)
            contents = self.api_model.batch_chat(prompts, temperature=1)
            # Normalize contents to list[str]
            if contents is None:
                contents = []
            if not isinstance(contents, list):
                contents = [contents]

            normalized = []
            for c in contents:
                if not isinstance(c, str):
                    c = "" if c is None else str(c)
                normalized.append(c.replace('<format>', '').replace('</format>', ''))

            # If batch size mismatch, pad with empty strings
            if len(normalized) < len(prompts):
                normalized.extend([""] * (len(prompts) - len(normalized)))

            self.output_token_usage += self.token_counter.num_tokens_from_list_string(normalized)
            res_l[idx] = normalized
        except Exception as e:
            # Fail-safe: still set a placeholder to keep pipeline running (or let caller handle)
            res_l[idx] = [f"# ERROR generating section '{section}': {type(e).__name__}: {e}"]

    # ------------------------
    # Helpers
    # ------------------------
    def __generate_prompt(self, template: str, paras: Dict[str, Any]) -> str:
        """
        Replace placeholders in template with provided values.
        All values coerced to strings to avoid TypeError on replace.
        """
        prompt = template
        for k, v in paras.items():
            val = v if isinstance(v, str) else ("" if v is None else str(v))
            prompt = prompt.replace(f"[{k}]", val)
        return prompt

    def parse_outline(self, outline: str) -> Dict[str, Any]:
        """
        Parse outline text into sections/subsections and descriptions.
        Outline format assumed:
          # Title
          ## Section
          Description: ...
          ### Subsection
          Description: ...
        Lines must start with exact markers (no leading spaces).
        """
        result = {
            "title": "",
            "sections": [],
            "section_descriptions": [],
            "subsections": [],
            "subsection_descriptions": []
        }
        lines = outline.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("# "):
                result["title"] = line[2:].strip()
            elif line.startswith("## "):
                result["sections"].append(line[3:].strip())
                # Start arrays for this section when a description line follows (common in your format)
                if i + 1 < len(lines) and lines[i + 1].startswith("Description:"):
                    result["section_descriptions"].append(lines[i + 1].split("Description:", 1)[1].strip())
                else:
                    result["section_descriptions"].append("")
                # Always append containers so indices align
                result["subsections"].append([])
                result["subsection_descriptions"].append([])
            elif line.startswith("### "):
                # Attach to the latest section if exists
                if result["subsections"]:
                    result["subsections"][-1].append(line[4:].strip())
                    if i + 1 < len(lines) and lines[i + 1].startswith("Description:"):
                        result["subsection_descriptions"][-1].append(
                            lines[i + 1].split("Description:", 1)[1].strip()
                        )
                    else:
                        result["subsection_descriptions"][-1].append("")
        return result

    def _validate_parsed_outline(self, parsed: Dict[str, Any]) -> None:
        """
        Ensure parsed outline has at least one section and one subsection overall.
        """
        if not parsed.get("sections"):
            raise ValueError("parse_outline produced no sections. Check outline format.")
        total_subs = sum(len(x) for x in parsed.get("subsections", []))
        if total_subs == 0:
            raise ValueError("parse_outline produced no subsections. Check outline format (### and Description lines).")

    def convert_tree_md_to_json(self, md_lines: List[str]) -> Dict[str, Any]:
        """ Convert Markdown tree to nested dict. """
        tree: Dict[str, Any] = {}
        stack = [(tree, -1)]
        for line in md_lines:
            stripped = line.lstrip()
            if not stripped.startswith("|----"):
                continue
            indent = len(line) - len(stripped)
            node_text = stripped[5:].strip()
            while indent <= stack[-1][1]:
                stack.pop()
            parent_dict = stack[-1][0]
            parent_dict[node_text] = {}
            stack.append((parent_dict[node_text], indent))
        return tree

    def extract_rids_from_tree(self, md_lines: List[str]) -> List[str]:
        """ Extract all [RID:xxx] in first-appearance order. """
        pat = re.compile(r'\[RID:([^\]]+)\]')
        rid_order, seen = [], set()
        for line in md_lines:
            for rid in pat.findall(line):
                if rid not in seen:
                    seen.add(rid)
                    rid_order.append(rid)
        return rid_order

    def renumber_and_build_refs(self, unified_tree_md: str, rid_order: List[str]) -> str:
        """ Convert [RID:xxx] to [1],[2]... and build References section. """
        rid2num = {rid: i + 1 for i, rid in enumerate(rid_order)}

        def _repl(m):
            rid = m.group(1)
            return f"[{rid2num.get(rid, '?')}]"

        safe_text = unified_tree_md if isinstance(unified_tree_md, str) else ("" if unified_tree_md is None else str(unified_tree_md))
        final_tree = re.sub(r'\[RID:([^\]]+)\]', _repl, safe_text)

        refs = self.db.get_paper_info_from_ids(rid_order)
        id2meta = {p.get('id'): p for p in refs}
        lines = ["References"]
        for rid in rid_order:
            meta = id2meta.get(rid)
            if not meta and "v" in rid:  # Try ignoring version suffix
                base_id = rid.split("v")[0]
                meta = id2meta.get(base_id)
            if not meta:
                lines.append(f"[{rid2num[rid]}] Missing metadata for {rid}")
                continue
            authors = ", ".join(meta.get("authors", []) or []) or "Unknown"
            year = meta.get("year", "n.d.")
            title = meta.get("title", "(No title)")
            venue = meta.get("venue", "arXiv")
            doi = meta.get("doi", "")
            entry = f"[{rid2num[rid]}] {authors} ({year}). {title}. {venue}."
            if doi:
                entry += f" https://doi.org/{doi}"
            lines.append(entry)

        return final_tree + "\n\n" + "\n".join(lines)