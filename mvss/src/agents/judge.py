import re
import random
import hashlib
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Optional, Tuple

import numpy as np
from tqdm import tqdm

from src.model import APIModel


CRITERIA = {
    "Coverage": {
        "description": "Coverage assesses whether the survey covers key and peripheral aspects comprehensively.",
        "score 1": "Very limited coverage; misses most key areas.",
        "score 2": "Covers some parts but with major omissions.",
        "score 3": "Generally comprehensive but misses a few important points.",
        "score 4": "Covers most key areas; only minor topics missing.",
        "score 5": "Fully comprehensive; covers key and peripheral topics in depth.",
    },
    "Structure": {
        "description": "Structure evaluates logical organization, coherence, and non-redundant flow.",
        "score 1": "No clear logic or connections between sections.",
        "score 2": "Weak flow; disordered organization in places.",
        "score 3": "Mostly reasonable; some transitions/redundancy issues.",
        "score 4": "Good logical consistency; minor rigidity.",
        "score 5": "Tightly structured, clear logic, smooth transitions, no redundancy.",
    }, 
    "Relevance": {
        "description": "Relevance measures alignment with topic and focus; minimal digressions.",
        "score 1": "Outdated/unrelated; not aligned with the topic.",
        "score 2": "Somewhat on topic but frequent digressions.",
        "score 3": "Generally on topic with a few unrelated details.",
        "score 4": "Mostly focused; infrequent digressions.",
        "score 5": "Exceptionally focused; every detail supports understanding of the topic.",
    },
    "TreeQuality": {
        "description": "TreeQuality evaluates taxonomy/topic tree: hierarchy correctness, coverage, clarity.",
        "score 1": "No meaningful tree or totally wrong hierarchy.",
        "score 2": "Partial tree with major missing branches or confusing structure.",
        "score 3": "Reasonable tree but missing important branches or unclear grouping.",
        "score 4": "Good tree with minor issues.",
        "score 5": "Excellent tree: comprehensive, correct, clear grouping, useful abstraction.",
    },
    "TableQuality": {
        "description": "TableQuality evaluates comparison tables: correctness, completeness, consistency, usefulness.",
        "score 1": "No usable table or table is incorrect/misleading.",
        "score 2": "Table exists but incomplete/inconsistent/hard to use.",
        "score 3": "Usable but missing key dimensions or some inconsistencies.",
        "score 4": "Good tables with minor omissions.",
        "score 5": "Excellent tables: comprehensive comparisons and consistent formatting.",
    },
}

CRITERIA_BASED_JUDGING_PROMPT = """
Here is an academic survey about the topic "[TOPIC]":
---
[SURVEY]
---

<instruction>
Please evaluate this survey based on the criterion below and give a score from 1 to 5 according to the score descriptions.

Criterion Description: [Criterion Description]

Score 1 Description: [Score 1 Description]
Score 2 Description: [Score 2 Description]
Score 3 Description: [Score 3 Description]
Score 4 Description: [Score 4 Description]
Score 5 Description: [Score 5 Description]

Return the score WITHOUT any other information.
</instruction>
""".strip()

NLI_PROMPT = """
Claim:
[CLAIM]

Source:
[SOURCE]

Is the Claim faithful to the Source?
A Claim is faithful if the core of the claim is supported by the Source.

Only reply with 'Yes' or 'No'.
""".strip()


@dataclass
class CitationEvalConfig:
    max_claims: int = 0
    max_sources_per_claim: int = 0
    max_precision_checks: int = 0
    max_workers: int = 8
    seed: int = 42

    use_title_citations: bool = True
    use_numeric_citations: bool = True

    skip_tables: bool = True
    skip_code_blocks: bool = True


class Judge:
    def __init__(
        self,
        model: str,
        api_key: str,
        api_url: str,
        database=None,
        nli_model: Optional[str] = None,
        nli_api_url: Optional[str] = None,
        verbose: bool = False,
    ) -> None:
        self.model = model
        self.api_key = api_key
        self.api_url = api_url
        self.db = database

        self.api_model = APIModel(self.model, self.api_key, self.api_url)

        self.nli_model_name = nli_model or model
        self.nli_api_url = nli_api_url or api_url
        self.nli_api_model = APIModel(self.nli_model_name, self.api_key, self.nli_api_url)

        self.last_citation_stats: Dict[str, object] = {}
        self._nli_cache: Dict[str, str] = {}

    def _gen_prompt(self, template: str, content_paras: Dict[str, str]) -> str:
        out = template
        for k, v in content_paras.items():
            out = out.replace(f"[{k}]", str(v))
        return out

    def extract_num(self, s: str) -> int:
        nums = re.findall(r"\d+", s or "")
        if not nums:
            return 0
        v = int(nums[0])
        return max(1, min(5, v))

    def _hash(self, s: str) -> str:
        return hashlib.md5(s.encode("utf-8")).hexdigest()

    def _score_one_criterion_fulltext(self, topic: str, survey_text: str, criterion: str) -> int:
        c = CRITERIA[criterion]
        prompt = self._gen_prompt(
            CRITERIA_BASED_JUDGING_PROMPT,
            {
                "TOPIC": topic,
                "SURVEY": survey_text,
                "Criterion Description": c["description"],
                "Score 1 Description": c["score 1"],
                "Score 2 Description": c["score 2"],
                "Score 3 Description": c["score 3"],
                "Score 4 Description": c["score 4"],
                "Score 5 Description": c["score 5"],
            },
        )
        resp = self.api_model.chat(prompt, temperature=0.0)
        return self.extract_num(resp)

    def batch_criteria_based_judging(
        self,
        survey_text: str,
        topic: str,
        criteria: List[str],
        show_progress: bool = True,
    ) -> List[int]:
        scores = [0] * len(criteria)
        with ThreadPoolExecutor(max_workers=min(8, max(1, len(criteria)))) as ex:
            futs = {ex.submit(self._score_one_criterion_fulltext, topic, survey_text, c): i
                    for i, c in enumerate(criteria)}
            it = as_completed(futs)
            if show_progress:
                it = tqdm(it, total=len(futs), desc="Scoring base criteria", leave=True)
            for fut in it:
                i = futs[fut]
                try:
                    scores[i] = int(fut.result() or 0)
                except Exception:
                    scores[i] = 0
        return scores

    def extract_taxonomy_tree(self, survey_text: str) -> str:
        lines = survey_text.splitlines()
        pat = re.compile(r"^#{2,4}\s+.*(taxonomy|tree|hierarchy|topic\s*tree).*", re.IGNORECASE)
        idx = None
        for i, line in enumerate(lines):
            if pat.match(line.strip()):
                idx = i
                break
        if idx is None:
            return ""
        out = [lines[idx]]
        for j in range(idx + 1, len(lines)):
            if re.match(r"^#{2,4}\s+", lines[j]) and j > idx + 1:
                break
            out.append(lines[j])
        return "\n".join(out).strip()

    def _score_text_on_criterion(self, text: str, topic: str, criterion: str) -> int:
        c = CRITERIA[criterion]
        prompt = self._gen_prompt(
            CRITERIA_BASED_JUDGING_PROMPT,
            {
                "TOPIC": topic,
                "SURVEY": text,
                "Criterion Description": c["description"],
                "Score 1 Description": c["score 1"],
                "Score 2 Description": c["score 2"],
                "Score 3 Description": c["score 3"],
                "Score 4 Description": c["score 4"],
                "Score 5 Description": c["score 5"],
            },
        )
        resp = self.api_model.chat(prompt, temperature=0.0)
        return self.extract_num(resp)

    def score_tree_all(
        self,
        survey_text: str,
        topic: str,
        chunk_chars: int = 12000,
        max_workers: int = 2,
        show_progress: bool = True,
    ) -> int:
        tree = self.extract_taxonomy_tree(survey_text)
        if not tree.strip():
            return 1

        chunks = [tree[i:i + chunk_chars] for i in range(0, len(tree), chunk_chars)]
        vals: List[int] = []

        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futs = [ex.submit(self._score_text_on_criterion, ch, topic, "TreeQuality") for ch in chunks]
            it = as_completed(futs)
            if show_progress:
                it = tqdm(it, total=len(futs), desc="Scoring tree", leave=True)
            for fut in it:
                try:
                    v = int(fut.result() or 0)
                except Exception:
                    v = 0
                if v:
                    vals.append(v)
        return int(round(float(np.mean(vals)))) if vals else 0

    def extract_markdown_tables_list(
        self,
        text: str,
        max_tables: int = 999,
        max_rows_per_table: int = 200,
    ) -> List[str]:
        lines = text.splitlines()
        tables: List[str] = []
        cur: List[str] = []

        def flush():
            nonlocal cur
            if cur:
                tables.append("\n".join(cur[:max_rows_per_table]).strip())
                cur = []

        for line in lines:
            if "|" in line:
                cur.append(line)
            else:
                flush()
        flush()

        valid: List[str] = []
        for t in tables:
            rows = t.splitlines()
            if len(rows) >= 2 and re.search(r"\|\s*[-:]+\s*\|", rows[1]):
                valid.append(t)
        return valid[:max_tables]

    def score_tables_bucketed(
        self,
        survey_text: str,
        topic: str,
        bucket_chars: int = 12000,
        max_workers: int = 2,
        max_tables: int = 999,
        max_rows: int = 200,
        show_progress: bool = True,
    ) -> int:
        tables = self.extract_markdown_tables_list(
            survey_text, max_tables=max_tables, max_rows_per_table=max_rows
        )
        if not tables:
            return 1

        buckets: List[str] = []
        cur: List[str] = []
        cur_len = 0
        for t in tables:
            t = t.strip()
            if not t:
                continue
            add_len = len(t) + (2 if cur else 0)
            if cur and (cur_len + add_len > max(2000, bucket_chars)):
                buckets.append("\n\n---\n\n".join(cur))
                cur = [t]
                cur_len = len(t)
            else:
                cur.append(t)
                cur_len += add_len
        if cur:
            buckets.append("\n\n---\n\n".join(cur))

        vals: List[int] = []
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futs = [ex.submit(self._score_text_on_criterion, b, topic, "TableQuality") for b in buckets]
            it = as_completed(futs)
            if show_progress:
                it = tqdm(it, total=len(futs), desc="Scoring tables", leave=True)
            for fut in it:
                try:
                    v = int(fut.result() or 0)
                except Exception:
                    v = 0
                if v:
                    vals.append(v)
        return int(round(float(np.mean(vals)))) if vals else 0

    def _strip_tables(self, text: str) -> str:
        return re.sub(r"^\|.*\|\s*$", "", text, flags=re.MULTILINE)

    def _strip_code_blocks(self, text: str) -> str:
        return re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    def _parse_citations_from_sentence(self, sentence: str) -> List[str]:
        br = re.findall(r"\[(.*?)\]", sentence)
        out: List[str] = []
        for b in br:
            parts = [x.strip() for x in b.split(";")]
            out.extend([p for p in parts if p])
        return out

    def _resolve_citation_token(
        self,
        token: str,
        num_map: Dict[int, str],
        title_map: Dict[str, str],
    ) -> Optional[str]:
        m = re.findall(r"\d+", token)
        if m:
            return num_map.get(int(m[0]))
        t = re.sub(r"\s+", " ", token.strip())
        return title_map.get(t)

    def _old_nli_yesno(self, claim: str, sources_abs_list: List[str]) -> int:
        src = "\n".join([s for s in sources_abs_list if s and s.strip()])
        if not src.strip():
            return 0

        key = self._hash("old_nli||" + claim + "||" + self._hash(src))
        if key in self._nli_cache:
            return 1 if self._nli_cache[key] == "yes" else 0

        prompt = self._gen_prompt(NLI_PROMPT, {"CLAIM": claim, "SOURCE": src})
        res = (self.nli_api_model.chat(prompt, temperature=0.0) or "").strip().lower()
        ans = "yes" if "yes" in res else "no"

        self._nli_cache[key] = ans
        return 1 if ans == "yes" else 0

    def _old_relevant_credit(self, claim: str, one_source_abs: str, complement_abs_list: List[str]) -> int:
        credit_one = self._old_nli_yesno(claim, [one_source_abs])
        if credit_one == 1:
            return 1

        credit_com = self._old_nli_yesno(claim, complement_abs_list)
        if credit_com == 1:
            return 0
        return 1

    def citation_quality(
        self,
        survey_text: str,
        references: Dict[str, str],
        cfg: Optional[CitationEvalConfig] = None,
        show_progress: bool = True,
    ) -> Tuple[float, float]:
        cfg = cfg or CitationEvalConfig()

        main_text = survey_text.split("## References")[0]

        if cfg.skip_code_blocks:
            main_text = self._strip_code_blocks(main_text)
        if cfg.skip_tables:
            main_text = self._strip_tables(main_text)

        sent_pat = re.compile(r"[^.!?。！？]*\[[^\]]+\][^.!?。！？]*[.!?。！？]")
        sentences = sent_pat.findall(main_text)

        num_map: Dict[int, str] = {}
        title_map: Dict[str, str] = {}
        for k, v in (references or {}).items():
            ks = str(k).strip()
            if ks.isdigit():
                num_map[int(ks)] = v
            else:
                title_map[re.sub(r"\s+", " ", ks)] = v

        claims: List[str] = []
        claim_source_pids: List[List[str]] = []
        unresolved = 0
        resolved = 0

        for s in sentences:
            tokens = self._parse_citations_from_sentence(s)
            if not tokens:
                continue

            pids: List[str] = []
            for tok in tokens:
                pid = None
                if cfg.use_numeric_citations:
                    pid = self._resolve_citation_token(tok, num_map, title_map)
                if pid is None and cfg.use_title_citations:
                    pid = self._resolve_citation_token(tok, {}, title_map)

                if pid is None:
                    unresolved += 1
                    continue
                resolved += 1
                pids.append(pid)

            pids = list(dict.fromkeys(pids))
            if not pids:
                continue

            claim = re.sub(r"\[(.*?)\]", "", s).strip()
            claims.append(claim)
            claim_source_pids.append(pids)

        total_claims_found = len(claims)

        rng = random.Random(cfg.seed)
        idxs = list(range(total_claims_found))
        if cfg.max_claims and cfg.max_claims > 0 and total_claims_found > cfg.max_claims:
            idxs = rng.sample(idxs, cfg.max_claims)
            idxs.sort()

        claims_eval = [claims[i] for i in idxs]
        sources_eval = [claim_source_pids[i] for i in idxs]

        all_ids = sorted({pid for sids in sources_eval for pid in sids})
        paper_infos = self.db.get_paper_info_from_ids(all_ids) if (self.db is not None and all_ids) else []
        id_to_abs = {p["id"]: (p.get("abs") or "") for p in paper_infos}

        recall_flags = [0] * len(claims_eval)

        def recall_job(i: int) -> int:
            claim = claims_eval[i]
            sids = sources_eval[i]
            if cfg.max_sources_per_claim and cfg.max_sources_per_claim > 0:
                sids = sids[: cfg.max_sources_per_claim]
            src_list = [id_to_abs.get(pid, "") for pid in sids if id_to_abs.get(pid, "")]
            return self._old_nli_yesno(claim, src_list)

        with ThreadPoolExecutor(max_workers=cfg.max_workers) as ex:
            futs = {ex.submit(recall_job, i): i for i in range(len(claims_eval))}
            it = as_completed(futs)
            if show_progress:
                it = tqdm(it, total=len(futs), desc="Citation recall (old logic)", leave=True)
            for fut in it:
                i = futs[fut]
                try:
                    recall_flags[i] = int(fut.result() or 0)
                except Exception:
                    recall_flags[i] = 0

        recall = float(np.mean(recall_flags)) if recall_flags else 0.0

        citations_total_all = sum(len(sids) for sids in sources_eval)
        precision_credit = 0

        tasks: List[Tuple[str, str, List[str]]] = []
        for j, ok in enumerate(recall_flags):
            if ok != 1:
                continue
            claim = claims_eval[j]
            pids = sources_eval[j]
            for pid in pids:
                others = [x for x in pids if x != pid]
                tasks.append((claim, pid, others))

        if cfg.max_precision_checks and cfg.max_precision_checks > 0 and len(tasks) > cfg.max_precision_checks:
            tasks = rng.sample(tasks, cfg.max_precision_checks)

        def prec_job(item: Tuple[str, str, List[str]]) -> int:
            claim, pid, others = item
            one = id_to_abs.get(pid, "")
            comps = [id_to_abs.get(x, "") for x in others if id_to_abs.get(x, "")]
            if not one.strip():
                return 0
            return self._old_relevant_credit(claim, one, comps)

        if tasks:
            with ThreadPoolExecutor(max_workers=cfg.max_workers) as ex:
                futs = [ex.submit(prec_job, it) for it in tasks]
                it2 = as_completed(futs)
                if show_progress:
                    it2 = tqdm(it2, total=len(futs), desc="Citation precision (old logic)", leave=True)
                for fut in it2:
                    try:
                        precision_credit += int(fut.result() or 0)
                    except Exception:
                        pass

        precision = (precision_credit / float(citations_total_all)) if citations_total_all > 0 else 0.0

        self.last_citation_stats = {
            "claims_found": total_claims_found,
            "claims_evaluated": len(claims_eval),
            "citations_total_all_claims": citations_total_all,
            "resolved_citations": resolved,
            "unresolved_citations": unresolved,
            "precision_tasks": len(tasks),
            "precision_mode": "strict_old_logic",
            "recall_mode": "old_logic",
            "skip_tables": cfg.skip_tables,
            "skip_code_blocks": cfg.skip_code_blocks,
            "nli_model": self.nli_model_name,
        }

        return recall, precision