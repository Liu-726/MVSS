import os
import glob
import json
import argparse
from datetime import datetime
from typing import List, Tuple, Any, Dict, Optional

from tqdm import tqdm

from src.database import database
from src.agents.judge import Judge, CitationEvalConfig


def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate AutoSurvey outputs (single topic or a whole directory)")

    parser.add_argument("--gpu", default="0", type=str, help="Specify the GPU to use (if needed)")
    parser.add_argument("--saving_path", default="./output/", type=str, help="Directory containing survey JSON files")
    parser.add_argument("--model", default="gpt-4o-2024-05-13", type=str, help="Model for evaluation")
    parser.add_argument(
        "--topic",
        default="",
        type=str,
        help="If set, only evaluate {topic}.json; otherwise evaluate ALL .json under saving_path",
    )

    parser.add_argument(
        "--api_url",
        default="https://api.openai.com/v1/chat/completions",
        type=str,
        help="url for API request",
    )
    parser.add_argument("--api_key", default="", type=str, help="API key for the model")

    parser.add_argument("--db_path", default="./database", type=str, help="Directory of the database.")
    parser.add_argument(
        "--embedding_model",
        default="nomic-ai/nomic-embed-text-v1",
        type=str,
        help="Embedding model for retrieval.",
    )

    parser.add_argument(
        "--nli_model",
        default="",
        type=str,
        help="(Optional) model for citation NLI; default: same as --model",
    )
    parser.add_argument(
        "--nli_api_url",
        default="",
        type=str,
        help="(Optional) API url for NLI model; default: same as --api_url",
    )

    parser.add_argument("--recursive", action="store_true", help="Recursively search for *.json under saving_path")

    parser.add_argument("--max_claims", default=0, type=int, help="Max cited sentences to evaluate; 0 => all")
    parser.add_argument(
        "--max_sources_per_claim",
        default=0,
        type=int,
        help="Max sources per claim in recall NLI; 0 => all",
    )
    parser.add_argument(
        "--max_precision_checks",
        default=0,
        type=int,
        help="Max per-citation checks for precision; 0 => all",
    )
    parser.add_argument("--citation_workers", default=8, type=int, help="Max concurrent NLI calls")
    parser.add_argument("--seed", default=42, type=int, help="Sampling seed (only matters if any max_* > 0)")

    parser.add_argument(
        "--citation_include_tables",
        action="store_true",
        help="Include markdown tables when extracting cited sentences",
    )
    parser.add_argument(
        "--citation_include_code",
        action="store_true",
        help="Include code blocks when extracting cited sentences",
    )

    return parser.parse_args()


def is_candidate_json(path: str) -> bool:
    base = os.path.basename(path)
    if not base.endswith(".json"):
        return False
    lower = base.lower()
    if lower.endswith("_tree.json"):
        return False
    if "_evaluation" in lower:
        return False
    if lower in ("evaluation_summary.jsonl",):
        return False
    return True


def collect_json_files(args) -> List[str]:
    if args.topic:
        return [os.path.join(args.saving_path, f"{args.topic}.json")]

    if args.recursive:
        pattern = os.path.join(args.saving_path, "**", "*.json")
        all_json = glob.glob(pattern, recursive=True)
    else:
        pattern = os.path.join(args.saving_path, "*.json")
        all_json = glob.glob(pattern)

    return sorted([p for p in all_json if is_candidate_json(p)])


def _is_nonempty_str(x: Any) -> bool:
    return isinstance(x, str) and x.strip() != ""


def _join_sections(sections: Any) -> Optional[str]:
    """
    Try to convert section-like structures into a single survey string.
    Supports:
      - [{"heading":..., "text":...}, ...]
      - [{"title":..., "content":...}, ...]
      - [{"text":...}, ...]
      - dict with {"sections":[...]}
    """
    if isinstance(sections, dict) and "sections" in sections:
        sections = sections.get("sections")

    if not isinstance(sections, list) or not sections:
        return None

    chunks = []
    for s in sections:
        if isinstance(s, str):
            if s.strip():
                chunks.append(s.strip())
            continue
        if not isinstance(s, dict):
            continue

        heading = s.get("heading") or s.get("title") or s.get("section_title") or s.get("name")
        text = s.get("text") or s.get("content") or s.get("body")
        if _is_nonempty_str(heading) and _is_nonempty_str(text):
            chunks.append(f"{heading.strip()}\n{text.strip()}")
        elif _is_nonempty_str(text):
            chunks.append(text.strip())
        elif _is_nonempty_str(heading):
            chunks.append(heading.strip())

    out = "\n\n".join(chunks).strip()
    return out if out else None


def _find_first_text_field(dic: Dict[str, Any]) -> Optional[str]:
    """
    Heuristic: find a plausible survey text in various common keys,
    including hireview-style outputs.
    """
    if _is_nonempty_str(dic.get("survey")):
        return dic["survey"]

    survey_obj = dic.get("survey")
    if isinstance(survey_obj, dict):
        for k in ["text", "content", "body", "final", "output"]:
            if _is_nonempty_str(survey_obj.get(k)):
                return survey_obj[k]
        joined = _join_sections(survey_obj.get("sections") or survey_obj)
        if _is_nonempty_str(joined):
            return joined

    candidate_keys = [
        "hireview",
        "hiReview",
        "review",
        "output",
        "result",
        "final",
        "final_survey",
        "survey_text",
        "survey_output",
        "answer",
        "response",
        "generation",
        "content",
        "text",
        "body",
        "markdown",
    ]
    for k in candidate_keys:
        if _is_nonempty_str(dic.get(k)):
            return dic[k]

    joined = _join_sections(dic.get("sections"))
    if _is_nonempty_str(joined):
        return joined

    try:
        choices = dic.get("choices")
        if isinstance(choices, list) and choices:
            msg = choices[0].get("message") if isinstance(choices[0], dict) else None
            if isinstance(msg, dict) and _is_nonempty_str(msg.get("content")):
                return msg["content"]
    except Exception:
        pass

    return None


def _normalize_references(refs: Any) -> Dict[str, Any]:
    """
    Normalize references into a dict.
    Accept dict directly, or try to convert list into dict.
    If cannot, return {}.
    """
    if isinstance(refs, dict):
        return refs

    if isinstance(refs, list):
        out = {}
        idx = 1
        for item in refs:
            key = f"[{idx}]"
            if isinstance(item, str):
                out[key] = item
                idx += 1
            elif isinstance(item, dict):
                val = item.get("text") or item.get("content") or item.get("title") or item.get("raw") or str(item)
                out[key] = val
                idx += 1
            else:
                out[key] = str(item)
                idx += 1
        return out

    if isinstance(refs, str) and refs.strip():
        return {"[1]": refs.strip()}

    return {}


def read_survey_json(json_path: str) -> Tuple[str, dict]:
    """
    Compatible with:
      - AutoSurvey outputs: {"survey": "...", "reference"/"references": {...}}
      - hireview-like outputs with different text keys and/or sections
    """
    with open(json_path, "r", encoding="utf-8") as f:
        dic = json.load(f)

    survey = _find_first_text_field(dic)
    if not _is_nonempty_str(survey):
        raise KeyError(
            "No survey text found. Expected keys like: 'survey', 'hireview', 'review', 'content', 'text', "
            "or a 'sections' list."
        )

    refs_raw = None
    for k in ["reference", "references", "ref", "refs", "bib", "bibliography", "citation_map", "citations"]:
        if k in dic:
            refs_raw = dic.get(k)
            break

    if refs_raw is None and isinstance(dic.get("survey"), dict):
        for k in ["reference", "references", "ref", "refs", "bib", "bibliography", "citation_map", "citations"]:
            if k in dic["survey"]:
                refs_raw = dic["survey"].get(k)
                break

    references = _normalize_references(refs_raw)

    return survey, references


def evaluate_one(
    judge: Judge,
    topic: str,
    survey: str,
    references: dict,
    out_txt_path: str,
    citation_cfg: CitationEvalConfig,
    run_ts: str,
):
    base_criteria = ["Coverage", "Structure", "Relevance"]
    base_scores = judge.batch_criteria_based_judging(
        survey_text=survey,
        topic=topic,
        criteria=base_criteria,
        show_progress=True,
    )

    tree_score = judge.score_tree_all(survey_text=survey, topic=topic, show_progress=True)
    table_score = judge.score_tables_bucketed(survey_text=survey, topic=topic, show_progress=True)

    recall, precision = judge.citation_quality(survey, references, cfg=citation_cfg, show_progress=True)

    result = f"[{run_ts}] Judged by {judge.model}:\n"
    for c, s in zip(base_criteria, base_scores):
        result += f"{c} = {int(s)}\n"
    result += f"TreeQuality = {int(tree_score)}\n"
    result += f"TableQuality = {int(table_score)}\n"
    result += f"Citation Recall = {recall:.4f}\nCitation Precision = {precision:.4f}\n"
    result += f"Citation Stats = {json.dumps(getattr(judge, 'last_citation_stats', {}), ensure_ascii=False)}\n"
    result += "-" * 60 + "\n"

    with open(out_txt_path, "a+", encoding="utf-8") as f:
        f.write(result)

    return {
        "run_ts": run_ts,
        "topic": topic,
        "criteria_model": judge.model,
        "nli_model": judge.nli_model_name,
        "coverage": int(base_scores[0]) if len(base_scores) > 0 else 0,
        "structure": int(base_scores[1]) if len(base_scores) > 1 else 0,
        "relevance": int(base_scores[2]) if len(base_scores) > 2 else 0,
        "tree_quality": int(tree_score),
        "table_quality": int(table_score),
        "citation_recall": float(recall),
        "citation_precision": float(precision),
        "citation_stats": getattr(judge, "last_citation_stats", {}),
        "out_txt": out_txt_path,
    }


def main(args):
    if not os.path.exists(args.saving_path):
        raise FileNotFoundError(f"saving_path not found: {args.saving_path}")

    db = database(db_path=args.db_path, embedding_model=args.embedding_model)

    nli_model = args.nli_model.strip() or None
    nli_api_url = args.nli_api_url.strip() or None

    judge = Judge(
        model=args.model,
        api_key=args.api_key,
        api_url=args.api_url,
        database=db,
        nli_model=nli_model,
        nli_api_url=nli_api_url,
    )

    json_files = collect_json_files(args)
    if not json_files:
        print(f"No candidate survey json files found in: {args.saving_path}")
        return

    run_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    citation_cfg = CitationEvalConfig(
        max_claims=args.max_claims,
        max_sources_per_claim=args.max_sources_per_claim,
        max_precision_checks=args.max_precision_checks,
        max_workers=args.citation_workers,
        seed=args.seed,
        use_title_citations=True,
        use_numeric_citations=True,
        skip_tables=(not args.citation_include_tables),
        skip_code_blocks=(not args.citation_include_code),
    )

    summary_path = os.path.join(args.saving_path, "evaluation_summary.jsonl")
    with open(summary_path, "a+", encoding="utf-8") as sf:
        for json_path in tqdm(json_files, desc="Evaluating topics"):
            base = os.path.splitext(os.path.basename(json_path))[0]
            topic = base[:-8] if base.lower().endswith("_hireview") else base

            out_txt = os.path.join(os.path.dirname(json_path), f"{topic}_evaluation.txt")

            try:
                survey, refs = read_survey_json(json_path)
            except Exception as e:
                print(f"[SKIP] {json_path} read failed: {e}")
                continue

            try:
                record = evaluate_one(
                    judge=judge,
                    topic=topic,
                    survey=survey,
                    references=refs,
                    out_txt_path=out_txt,
                    citation_cfg=citation_cfg,
                    run_ts=run_ts,
                )
                sf.write(json.dumps(record, ensure_ascii=False) + "\n")
            except Exception as e:
                print(f"[ERROR] evaluating {json_path}: {e}")

    print(f"Done. Summary appended to: {summary_path}")


if __name__ == "__main__":
    args = parse_args()
    main(args)