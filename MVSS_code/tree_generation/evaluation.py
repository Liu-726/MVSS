import os
import re
import json
import argparse

from src.model import APIModel
from src.database import database
from src.prompt import NLI_PROMPT


def paras_args():
    parser = argparse.ArgumentParser(description='Evaluate citation recall/precision of a generated tree')
    parser.add_argument('--gpu', default='0', type=str, help='Specify the GPU to use')
    parser.add_argument('--saving_path', default='./output/', type=str, help='Directory containing outputs')
    parser.add_argument('--model', default='gpt-4o-2024-05-13', type=str, help='Model for evaluation')
    parser.add_argument('--topic', default='', type=str, help='Topic of the tree (filename prefix without extension)')
    parser.add_argument('--api_url', default='https://api.openai.com/v1/chat/completions', type=str, help='API URL')
    parser.add_argument('--api_key', default='', type=str, help='API key')
    parser.add_argument('--db_path', default='./database', type=str, help='DB directory')
    parser.add_argument('--embedding_model', default='nomic-ai/nomic-embed-text-v1', type=str, help='Embedding model')
    parser.add_argument('--max_leaves', default=200, type=int, help='Max number of leaf nodes to NLI-evaluate')
    args = parser.parse_args()
    return args


def read_tree_md_and_json(path, topic):
    md_path = os.path.join(path, f"{topic}_tree.md")
    json_path = os.path.join(path, f"{topic}_tree.json")
    if not os.path.exists(md_path):
        raise FileNotFoundError(f"Tree markdown not found: {md_path}")
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Tree JSON not found: {json_path}")

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    with open(json_path, 'r', encoding='utf-8') as f:
        j = json.load(f)
    rid_order = j.get("rid_order", [])
    tree_json = j.get("tree", {})
    return md_text, tree_json, rid_order


def parse_tree_md_leaves(md_text):
    lines = md_text.splitlines()

    section_pat = re.compile(r'^\|----Section\s+\d+:\s*(.+?)\s*$')
    subsection_pat = re.compile(r'^\|\s{5}\|----Subsection\s+\d+\.\d+:\s*(.+?)\s*$')
    keyword_pat = re.compile(r'^\|\s{5}\|\s{5}\|----\s*(.+?):\s*(.*)$')
    cite_num_pat = re.compile(r'\[(\d+)\]')

    current_section = None
    current_subsection = None
    leaves = []

    for ln in lines:
        m_sec = section_pat.match(ln)
        if m_sec:
            current_section = m_sec.group(1).strip()
            continue

        m_sub = subsection_pat.match(ln)
        if m_sub:
            current_subsection = m_sub.group(1).strip()
            continue

        m_kw = keyword_pat.match(ln)
        if m_kw:
            kw = m_kw.group(1).strip()
            tail = m_kw.group(2).strip()
            nums = [int(x) for x in cite_num_pat.findall(tail)]
            leaves.append({
                'section': current_section or "",
                'subsection': current_subsection or "",
                'keyword': kw,
                'nums': nums
            })

    return leaves


def nli_support(api_model: APIModel, claim: str, source_text: str) -> bool:
    prompt = NLI_PROMPT.replace("[CLAIM]", claim).replace("[SOURCE]", source_text)
    try:
        ans = api_model.chat(prompt, temperature=0)
    except Exception:
        return False
    if not ans:
        return False
    ans = ans.strip().lower()
    return ("yes" in ans) and ("no" not in ans)


def compute_citation_metrics(api_model: APIModel, db: database, leaves, rid_order, max_leaves=200):
    sample_leaves = leaves[:max_leaves] if max_leaves > 0 else leaves

    def nums_to_rids(nums):
        rids = []
        for n in nums:
            idx = n - 1
            if 0 <= idx < len(rid_order):
                rids.append(rid_order[idx])
        return rids

    all_rids = set()
    for item in sample_leaves:
        all_rids.update(nums_to_rids(item['nums']))
    all_rids = list(all_rids)

    papers = db.get_paper_info_from_ids(all_rids)
    id2abs = {p['id']: p.get('abs', '') for p in papers}

    leaf_supported_flags = []
    total_cites = 0
    supported_cites = 0

    for item in sample_leaves:
        claim = f"{item['section']} > {item['subsection']} : {item['keyword']}".strip()
        rids = nums_to_rids(item['nums'])

        any_support = False
        for rid in rids:
            src = id2abs.get(rid, "")
            total_cites += 1
            if not src:
                continue
            if nli_support(api_model, claim, src):
                supported_cites += 1
                any_support = True

        leaf_supported_flags.append(1 if any_support else 0)

    recall = (sum(leaf_supported_flags) / len(leaf_supported_flags)) if leaf_supported_flags else 0.0
    precision = (supported_cites / total_cites) if total_cites > 0 else 0.0
    return recall, precision


def evaluate(args):
    db = database(db_path=args.db_path, embedding_model=args.embedding_model)
    os.makedirs(args.saving_path, exist_ok=True)

    tree_md, tree_json, rid_order = read_tree_md_and_json(args.saving_path, args.topic)
    leaves = parse_tree_md_leaves(tree_md)

    api_model = APIModel(args.model, args.api_key, args.api_url)
    recall, precision = compute_citation_metrics(
        api_model, db, leaves, rid_order, max_leaves=args.max_leaves
    )

    out_path = os.path.join(args.saving_path, f"{args.topic}_citation_eval.txt")
    with open(out_path, 'a+', encoding='utf-8') as f:
        f.write(f"=== Citation Evaluation for: {args.topic} ===\n")
        f.write(f"Citation Recall = {recall:.4f}\n")
        f.write(f"Citation Precision = {precision:.4f}\n\n")

    print(f"[OK] Saved citation metrics to {out_path}")


if __name__ == '__main__':
    args = paras_args()
    evaluate(args)