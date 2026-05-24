import os
import json
import argparse
import re
import random
from typing import Dict, Tuple, List

from src.agents.outline_writer import outlineWriter
from src.agents.writer import TreeWriter
from src.agents.judge import Judge, CRITERIA
from src.agents.feedback_utils import build_feedback_instructions
from src.database import database

from evaluation import parse_tree_md_leaves, compute_citation_metrics
from src.model import APIModel


def remove_descriptions(text: str) -> str:
    lines = text.split('\n')
    filtered_lines = [line for line in lines if not line.strip().startswith("Description")]
    return '\n'.join(filtered_lines)


def write_outline(topic, model, section_num, outline_reference_num, db, api_key, api_url):
    outline_writer = outlineWriter(model=model, api_key=api_key, api_url=api_url, database=db)
    outline = outline_writer.draft_outline(topic, outline_reference_num, 30000, section_num)
    return outline, remove_descriptions(outline)


def paras_args():
    parser = argparse.ArgumentParser(description='Generate survey tree')
    parser.add_argument('--gpu', default='0', type=str, help='Specify the GPU to use')
    parser.add_argument('--saving_path', default='./tree_output/', type=str, help='Directory to save the output survey')
    parser.add_argument('--model', default='gpt-4o-2024-05-13', type=str, help='Model to use')
    parser.add_argument('--topic', default='', type=str, help='Topic to generate survey for')
    parser.add_argument('--section_num', default=7, type=int, help='Number of sections in the outline')
    parser.add_argument('--outline_reference_num', default=1500, type=int, help='Number of references for outline generation')

    parser.add_argument('--rag_num', default=60, type=int, help='Number of references to use for RAG (later rounds)')
    parser.add_argument('--rag_num_heavy', default=120, type=int, help='RAG size for the first iteration to support more citations')

    parser.add_argument('--api_url', default='https://api.openai.com/v1/chat/completions', type=str, help='URL for API request')
    parser.add_argument('--api_key', default='', type=str, help='API key for the model')
    parser.add_argument('--db_path', default='../database', type=str, help='Directory of the database.')
    parser.add_argument('--embedding_model', default='nomic-ai/nomic-embed-text-v1', type=str, help='Embedding model for retrieval.')
    parser.add_argument('--topic_txt', default='', type=str, help='TXT file containing multiple topics')

    parser.add_argument('--max_iterations', default=3, type=int, help='Maximum iterations for refinement (iter01..iter03)')
    parser.add_argument('--target_score', default=19, type=int, help='Target total score threshold (sum of 4 criteria)')

    parser.add_argument('--max_leaves_eval', default=200, type=int, help='Max leaf nodes to NLI-evaluate per iteration')

    parser.add_argument('--first_min_cites', default=3, type=int, help='First refinement iteration: min citations per leaf')
    parser.add_argument('--first_target_cites', default=5, type=int, help='First refinement iteration: target citations per leaf')
    parser.add_argument('--first_max_cites', default=6, type=int, help='First refinement iteration: max citations per leaf')

    parser.add_argument('--later_min_cites', default=1, type=int, help='Later refinement iterations: min citations per leaf')
    parser.add_argument('--later_target_cites', default=2, type=int, help='Later refinement iterations: target citations per leaf')
    parser.add_argument('--later_max_cites', default=3, type=int, help='Later refinement iterations: max citations per leaf')

    parser.add_argument('--model_gpt', default='gpt-4o', type=str)
    parser.add_argument('--api_url_gpt', default='https://api.openai.com/v1/chat/completions', type=str)
    parser.add_argument('--api_key_gpt', default='', type=str)

    parser.add_argument('--model_gemini', default='gemini-pro', type=str)
    parser.add_argument('--api_url_gemini', default='https://gemini-api-url.com', type=str)
    parser.add_argument('--api_key_gemini', default='', type=str)

    parser.add_argument('--model_claude', default='claude-3', type=str)
    parser.add_argument('--api_url_claude', default='https://claude-api-url.com', type=str)
    parser.add_argument('--api_key_claude', default='', type=str)

    parser.add_argument('--force_save_all_iters', action='store_true',
                        help='If set, will always run and save iter00..iter03 (no early stop).')

    args = parser.parse_args()
    return args


def read_topics_from_txt(txt_path):
    if not os.path.exists(txt_path):
        raise FileNotFoundError(f"TXT file not found: {txt_path}")
    with open(txt_path, 'r', encoding='utf-8') as f:
        topics = [line.strip() for line in f.readlines() if line.strip()]
    if not topics:
        raise ValueError(f"No valid topics in TXT file: {txt_path}")
    return topics


def _ensure_dirs(*paths):
    for p in paths:
        os.makedirs(p, exist_ok=True)


def _score_dict(criteria_names, scores_list, citation_recall=None, citation_precision=None, meta=None):
    d = {name: float(score) for name, score in zip(criteria_names, scores_list)}
    d["total"] = float(sum(scores_list))
    if citation_recall is not None:
        d["citation_recall"] = float(citation_recall)
    if citation_precision is not None:
        d["citation_precision"] = float(citation_precision)
    if meta:
        d["meta"] = meta
    return d


def _save_tree_and_scores(base_dir, safe_topic, tree_md, tree_json, rid_order, scores_dict):
    _ensure_dirs(base_dir)
    md_path = os.path.join(base_dir, f"{safe_topic}_tree.md")
    json_path = os.path.join(base_dir, f"{safe_topic}_tree.json")
    scores_path = os.path.join(base_dir, f"{safe_topic}_scores.json")

    with open(md_path, 'w', encoding='utf-8') as f_md:
        f_md.write(tree_md)

    with open(json_path, 'w', encoding='utf-8') as f_json:
        json.dump({
            "topic": safe_topic,
            "tree": tree_json,
            "rid_order": rid_order
        }, f_json, ensure_ascii=False, indent=4)

    with open(scores_path, 'w', encoding='utf-8') as f_scores:
        json.dump(scores_dict, f_scores, ensure_ascii=False, indent=4)

    print(f"Saved tree: {md_path}")
    print(f"Saved JSON: {json_path}")
    print(f"Saved scores: {scores_path}")


def _citation_policy_prompt(refine_round: int, args) -> str:
    if refine_round == 0:
        return (
            "[Citation Policy - Baseline (iter00): MORE citations]\n"
            f"- For EACH leaf node, include citations with a TARGET of {args.first_target_cites} "
            f"(MIN {args.first_min_cites}, MAX {args.first_max_cites}).\n"
            "- Use diverse, high-quality sources; avoid citing the same paper across many unrelated leaves.\n"
            "- Only use references available in the provided retrieval list (rid_order); do NOT invent sources.\n"
            "- Keep citations strictly formatted as bracketed indices [n] that map to rid_order.\n"
        )
    elif refine_round == 1:
        return (
            "[Citation Policy - Refinement Round 1 (iter01): MORE citations]\n"
            f"- For EACH leaf node, include citations with a TARGET of {args.first_target_cites} "
            f"(MIN {args.first_min_cites}, MAX {args.first_max_cites}).\n"
            "- Use diverse, high-quality sources; avoid citing the same paper across many unrelated leaves.\n"
            "- Only use references available in the provided retrieval list (rid_order); do NOT invent sources.\n"
            "- Keep citations strictly formatted as bracketed indices [n] that map to rid_order.\n"
        )
    else:
        return (
            "[Citation Policy - Later refinement rounds (iter02/iter03): FEWER but STRONGER]\n"
            f"- For EACH leaf node, include citations with a TARGET of {args.later_target_cites} "
            f"(MIN {args.later_min_cites}, MAX {args.later_max_cites}).\n"
            "- Prefer 1–2 highly supportive citations; remove weak or redundant ones.\n"
            "- Deduplicate aggressively; avoid over-using the same paper across many leaves.\n"
            "- Only use references from the provided rid_order; do NOT invent sources.\n"
            "- Keep bracketed index format [n] exactly.\n"
        )


def _build_targeted_feedback(scores, criteria_names, target_total=None):
    pairs = list(zip(criteria_names, [float(s) for s in scores]))
    vals = [p[1] for p in pairs]
    if not vals:
        return "No feedback: empty score vector."

    avg = sum(vals) / len(vals)
    min_val = min(vals)

    low = [name for name, v in pairs if (v < avg or v == min_val)]
    high = [name for name, v in pairs if name not in low]

    cookbook = {
        "Coverage": [
            "Add missing key branches/subtopics; expand sparse layers to ensure main trunks and the latest ~3 years of hotspots are covered.",
            "Attach seminal surveys/highly cited works as nodes; avoid listing only recent low-impact items.",
            "Incrementally expand the RAG pool by 10–20% relative to the previous round, while keeping existing high-importance nodes intact."
        ],
        "Structure": [
            "Normalize hierarchy depth (e.g., 3–4 levels); avoid mixing fine- and coarse-grained topics within the same level.",
            "Create cross-references for intersecting topics instead of hard-merging; reduce cycles and duplicate parent–child relations.",
            "Order nodes per level by: seminal surveys → core method families → applications/evaluation standards."
        ],
        "Relevance": [
            "Prune weakly related branches; add scope qualifiers for boundary topics (e.g., 'coreference in medical scenarios').",
            "Prefer citations within the same domain; use cross-domain papers only as contrast/insight nodes.",
            "Add one sentence per node explaining its direct relevance to the topic."
        ],
        "SalienceAlignment": [
            "Increase prominence of key nodes (bold/top/summary notes) and downweight minor nodes.",
            "When hotspot and niche nodes appear together, front-load the hotspot and give a one-line impact summary.",
            "For each main branch, add one sentence explaining 'why this is important' to avoid mere lists."
        ]
    }

    def bullets(names):
        lines = []
        for n in names:
            steps = cookbook.get(n, ["Apply targeted revisions for this dimension with limited scope to avoid harming already-strong dimensions."])
            lines.append(f"- {n}:\n  " + "\n  ".join([f"* {s}" for s in steps]))
        return "\n".join(lines) if lines else "- (none)"

    preserve_rules = [
        "Do not remove core nodes or their direct children under high-scoring dimensions.",
        "Allowed changes are limited to light textual refinements and cross-reference additions; node count change ≤ 5%.",
        "If hierarchy adjustment is necessary, ensure information is preserved (equivalent migration with a brief rationale)."
    ]

    target_hint = ""
    if target_total is not None:
        target_hint = f"(target total ≥ {target_total}, with no decrease in any high-scoring dimension)"

    text = []
    text.append("[Global Objectives]")
    text.append(f"- Perform an overall tree revision {target_hint}.")
    text.append("- Focus on low-scoring dimensions while keeping others stable or slightly improved; avoid global regressions.")
    text.append("")
    text.append("[Focus Areas: Actions for Low-Scoring Dimensions]")
    text.append(bullets(low))
    text.append("")
    text.append("[Preserve Areas: Constraints for High-Scoring Dimensions]")
    text.append("- Applicable dimensions: " + (", ".join(high) if high else "(none)"))
    text.append("  * " + "\n  * ".join(preserve_rules))
    text.append("")
    text.append("[Acceptance Criteria]")
    text.append("- Low-scoring dimensions show clear improvement compared to the previous round;")
    text.append("- High-scoring dimensions do not degrade;")
    text.append("- Total node count and depth remain within controlled range (±10% nodes / depth Δ ≤ 1);")
    text.append("- Provide a brief change log (1–2 sentences per modified branch).")

    return "\n".join(text)


def _sanitize_topic_to_filename(topic) -> str:
    if not isinstance(topic, str):
        topic = "" if topic is None else str(topic)
    s = topic.strip()
    if not s:
        s = "topic"
    s = re.sub(r'[\\/:*?"<>|\n\r\t]+', '_', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:120]


def write_outline_multi_models(
    topic: str,
    section_num: int,
    outline_reference_num: int,
    db,
    api_key_dict: Dict[str, str],
    api_url_dict: Dict[str, str],
    save_dir: str = "./debug_outlines"
) -> Tuple[str, str]:
    outlines = {}
    errors = {}
    model_list = ["gpt-4o", "gemini-2.5-pro", "claude-sonnet-4-20250514"]

    safe_topic = _sanitize_topic_to_filename(topic)
    topic_dir = os.path.join(save_dir, safe_topic)
    os.makedirs(topic_dir, exist_ok=True)

    valid_candidates = []

    for model_name in model_list:
        err_msg = None
        outline_text = ""
        try:
            ow = outlineWriter(
                model=model_name,
                api_key=api_key_dict[model_name],
                api_url=api_url_dict[model_name],
                database=db
            )
            outline_text = ow.draft_outline(topic, outline_reference_num, 30000, section_num)

            if not outline_text or not isinstance(outline_text, str) or len(outline_text) < 100:
                if outline_text:
                    outline_text = str(outline_text)
                else:
                    err_msg = "Empty or invalid response"
        except Exception as e:
            err_msg = f"{type(e).__name__}: {e}"
            outline_text = ""

        if err_msg:
            errors[model_name] = err_msg
            outlines[model_name] = ""
        else:
            outlines[model_name] = outline_text
            valid_candidates.append({"model": model_name, "text": outline_text})

        with open(os.path.join(topic_dir, f"{model_name}_outline.txt"), "w", encoding="utf-8") as f:
            f.write(outline_text or "")

    if not valid_candidates:
        with open(os.path.join(topic_dir, "errors.json"), "w", encoding="utf-8") as f:
            json.dump(errors, f, ensure_ascii=False, indent=2)
        raise RuntimeError(f"All outline generations failed for topic='{topic}'.")

    random.shuffle(valid_candidates)

    options_text = ""
    for idx, item in enumerate(valid_candidates):
        options_text += f"\n\n====== [Option {idx+1}] ======\n{item['text']}\n"

    gpt_judge_prompt = (
        f"You are an expert academic editor. There are {len(valid_candidates)} anonymous outline drafts for the survey topic \"{topic}\".\n"
        "Your task is to identify the single BEST outline that provides the most comprehensive, logical, and technically accurate structure.\n\n"
        "Evaluation Criteria:\n"
        "1. Coverage: Does it cover key sub-topics and recent advancements?\n"
        "2. Structure: Is the hierarchy (sections/sub-sections) logical and clear?\n"
        "3. Detail: Are the descriptions informative rather than generic?\n\n"
        f"{options_text}\n\n"
        "====== INSTRUCTIONS ======\n"
        "Step 1: Briefly analyze each Option (1-2 sentences on Pros/Cons).\n"
        "Step 2: Select the best option based on the criteria.\n"
        "Step 3: Output your final decision in exactly this format: [[BEST OPTION: X]]\n"
        "(Where X is the option number, e.g., 1, 2, or 3).\n\n"
        "Start your analysis now:"
    )

    with open(os.path.join(topic_dir, "judge_prompt.txt"), "w", encoding="utf-8") as f:
        f.write(gpt_judge_prompt)

    model_name_choice = "fallback"
    try:
        gpt_selector = outlineWriter(
            model="gpt-4o",
            api_key=api_key_dict["gpt-4o"],
            api_url=api_url_dict["gpt-4o"],
            database=db
        )
        response = gpt_selector.simple_call(gpt_judge_prompt)
        response = str(response).strip()

        with open(os.path.join(topic_dir, "judge_reasoning.txt"), "w", encoding="utf-8") as f:
            f.write(response)

        match = re.search(r'\[\[BEST OPTION:\s*([1-3])\]\]', response, re.IGNORECASE)
        if match:
            chosen_index = int(match.group(1)) - 1
            if 0 <= chosen_index < len(valid_candidates):
                best_candidate = valid_candidates[chosen_index]
                model_name_choice = best_candidate["model"]
                best_outline_text = best_candidate["text"]
            else:
                raise ValueError(f"Judge returned index {chosen_index+1} out of bounds.")
        else:
            raise ValueError("Could not find '[[BEST OPTION: X]]' tag in response.")

    except Exception as e:
        print(f"[Selection Failed] {e}. Falling back to longest outline.")
        best_candidate = max(valid_candidates, key=lambda x: len(x["text"]))
        model_name_choice = best_candidate["model"]
        best_outline_text = best_candidate["text"]
        errors["selector"] = str(e)
        with open(os.path.join(topic_dir, "selector_fallback_log.txt"), "w", encoding="utf-8") as f:
            f.write(f"Error: {e}\nFallback to: {model_name_choice}")

    with open(os.path.join(topic_dir, "selector_choice.txt"), "w", encoding="utf-8") as f:
        f.write(f"Selected: {model_name_choice}\n(Method: Blind Test + CoT)")

    cleaned = remove_descriptions(best_outline_text)
    with open(os.path.join(topic_dir, f"selected_{model_name_choice}_outline.cleaned.txt"), "w", encoding="utf-8") as f:
        f.write(cleaned)

    return best_outline_text, cleaned


def process_single_topic(topic, args, db):
    print(f"\n=== Processing topic: {topic} ===")

    api_key_dict = {
        "gpt-4o": args.api_key_gpt,
        "gemini-2.5-pro": args.api_key_gemini,
        "claude-sonnet-4-20250514": args.api_key_claude
    }
    api_url_dict = {
        "gpt-4o": args.api_url_gpt,
        "gemini-2.5-pro": args.api_url_gemini,
        "claude-sonnet-4-20250514": args.api_url_claude
    }

    outline_with_description, outline_wo_description = write_outline_multi_models(
        topic, args.section_num, args.outline_reference_num,
        db, api_key_dict, api_url_dict
    )

    tree_writer = TreeWriter(model=args.model, api_key=args.api_key, api_url=args.api_url, db=db)
    judge = Judge(model=args.model, api_key=args.api_key, api_url=args.api_url, database=db)
    api_model = APIModel(args.model, args.api_key, args.api_url)

    criteria_names = list(CRITERIA.keys())

    safe_topic = _sanitize_topic_to_filename(topic)
    per_iter_dir = os.path.join(args.saving_path, "per_iter")
    with_dir = os.path.join(args.saving_path, "with_re")
    without_dir = os.path.join(args.saving_path, "without_re")
    _ensure_dirs(per_iter_dir, with_dir, without_dir)

    all_iter_scores: List[dict] = []

    best_tree_md, best_tree_json, best_rid_order = None, None, None
    best_score_sum = -1.0
    best_scores_dict = None

    prev_feedback = ""

    total_needed = 3
    if args.max_iterations != 3:
        print(f"[WARN] You set --max_iterations={args.max_iterations}. "
              f"If you want exactly 4 trees (iter00..iter03), please set --max_iterations=3.")

    for refine_round in range(0, args.max_iterations + 1):
        iter_tag = f"iter{refine_round:02d}"
        print(f"\n--- {iter_tag} (refine_round={refine_round}) ---")

        citation_policy = _citation_policy_prompt(refine_round, args)
        merged_outline = citation_policy + "\n\n"

        if refine_round >= 1 and prev_feedback:
            merged_outline += "Feedback from previous round:\n" + prev_feedback + "\n\n"

        merged_outline += outline_with_description

        if refine_round in (0, 1):
            rag_this_round = args.rag_num_heavy
        else:
            rag_this_round = args.rag_num

        tree_md, tree_json, rid_order = tree_writer.write_tree(
            topic=topic,
            outline=merged_outline,
            rag_num=rag_this_round
        )

        if not isinstance(tree_md, str):
            raise TypeError(f"ERROR: tree_md is not str. type={type(tree_md)}, preview={repr(tree_md)[:200]}")

        scores = judge.batch_criteria_based_judging(
            survey=tree_md,
            topic=topic,
            criteria=criteria_names
        )
        score_sum = float(sum(scores))

        leaves = parse_tree_md_leaves(tree_md)
        c_recall, c_precision = compute_citation_metrics(
            api_model=api_model,
            db=db,
            leaves=leaves,
            rid_order=rid_order,
            max_leaves=args.max_leaves_eval
        )

        scores_dict = _score_dict(
            criteria_names, scores,
            citation_recall=c_recall,
            citation_precision=c_precision,
            meta={
                "iter_tag": iter_tag,
                "refine_round": refine_round,
                "rag_num_used": rag_this_round,
                "citation_policy": (
                    "baseline_more" if refine_round == 0 else
                    ("more@round1" if refine_round == 1 else "fewer_stronger@later")
                ),
                "first_target_cites": args.first_target_cites,
                "first_min_cites": args.first_min_cites,
                "first_max_cites": args.first_max_cites,
                "later_target_cites": args.later_target_cites,
                "later_min_cites": args.later_min_cites,
                "later_max_cites": args.later_max_cites
            }
        )

        all_iter_scores.append(scores_dict)

        print(f"{iter_tag} scores: {scores}, total={score_sum:.3f} | "
              f"citation recall={c_recall:.3f}, precision={c_precision:.3f}")

        iter_prefix = f"{safe_topic}_{iter_tag}"
        _save_tree_and_scores(
            base_dir=per_iter_dir,
            safe_topic=iter_prefix,
            tree_md=tree_md,
            tree_json=tree_json,
            rid_order=rid_order,
            scores_dict=scores_dict
        )

        if refine_round == 0:
            _save_tree_and_scores(
                base_dir=without_dir,
                safe_topic=safe_topic,
                tree_md=tree_md,
                tree_json=tree_json,
                rid_order=rid_order,
                scores_dict=scores_dict
            )

        if score_sum > best_score_sum:
            best_score_sum = score_sum
            best_tree_md, best_tree_json, best_rid_order = tree_md, tree_json, rid_order
            best_scores_dict = scores_dict

        if refine_round < args.max_iterations:
            feedback = _build_targeted_feedback(
                scores=scores,
                criteria_names=criteria_names,
                target_total=args.target_score
            )
            prev_feedback = feedback
            print("Generated Feedback (for next round):\n", feedback)

        if (not args.force_save_all_iters) and (refine_round >= 1) and (score_sum >= args.target_score):
            print(f"[Early Stop] target_score reached at {iter_tag}. (force_save_all_iters=False)")
            break

    scores_all_path = os.path.join(per_iter_dir, f"{safe_topic}_all_iters_scores.json")
    with open(scores_all_path, "w", encoding="utf-8") as f:
        json.dump(all_iter_scores, f, ensure_ascii=False, indent=2)
    print(f"Saved all-iter scores: {scores_all_path}")

    if best_tree_md is not None:
        print("[Save] Best result (with_re)")
        _save_tree_and_scores(
            base_dir=with_dir,
            safe_topic=safe_topic,
            tree_md=best_tree_md,
            tree_json=best_tree_json,
            rid_order=best_rid_order,
            scores_dict=best_scores_dict
        )


def main(args):
    db = database(db_path=args.db_path, embedding_model=args.embedding_model)
    os.makedirs(args.saving_path, exist_ok=True)

    if args.topic_txt:
        try:
            topics = read_topics_from_txt(args.topic_txt)
            print(f"Loaded {len(topics)} topics from TXT: {args.topic_txt}")
        except Exception as e:
            print(f"Error loading TXT: {str(e)}")
            return
    elif args.topic:
        topics = [args.topic]
        print(f"Processing single topic: {args.topic}")
    else:
        print("Error: Please specify --topic (single) or --topic_txt (batch)")
        return

    total_topics = len(topics)
    for idx, topic in enumerate(topics, 1):
        print(f"\n--- Progress: {idx}/{total_topics} ---")
        try:
            process_single_topic(topic, args, db)
        except Exception as e:
            print(f"Failed to process {topic}: {str(e)}")
            continue

    print(f"\nAll tasks completed! Total processed: {total_topics} topics")


if __name__ == '__main__':
    args = paras_args()
    main(args)