import os
import glob
import json
import argparse
from src.agents.outline_writer import outlineWriter
from src.agents.writer import subsectionWriter
from src.database import database

def remove_descriptions(text):
    lines = text.split('\n')
    filtered_lines = [line for line in lines if not line.strip().startswith("Description")]
    return '\n'.join(filtered_lines)

def write_outline(topic, model, section_num, outline_reference_num, db, api_key, api_url, prior_md_content="", prior_json_content=""):
    outline_writer = outlineWriter(model=model, api_key=api_key, api_url = api_url, database=db)
    outline = outline_writer.draft_outline(
        topic, outline_reference_num, 30000, section_num,
        prior_md_content=prior_md_content, prior_json_content=prior_json_content
    )
    return outline, remove_descriptions(outline)

def write_subsection(topic, model, outline, subsection_len, rag_num, db, api_key, api_url, refinement = True, prior_md_content="", prior_json_content=""):
    subsection_writer = subsectionWriter(model=model, api_key=api_key, api_url = api_url, database=db)
    return subsection_writer.write(
        topic, outline, subsection_len=subsection_len, rag_num=rag_num, refining=refinement,
        prior_md_content=prior_md_content, prior_json_content=prior_json_content
    )

def paras_args():
    parser = argparse.ArgumentParser(description='Auto Survey Generator')
    parser.add_argument('--gpu',default='0', type=str)
    parser.add_argument('--saving_path',default='./output/', type=str)
    parser.add_argument('--model',default='gpt-4o', type=str) 
    parser.add_argument('--topic',default='', type=str)
    parser.add_argument('--tree_dir',default='./tree_generation/tree_output', type=str)
    parser.add_argument('--section_num',default=5, type=int)
    parser.add_argument('--subsection_len',default=400, type=int)
    parser.add_argument('--outline_reference_num',default=1000, type=int)
    parser.add_argument('--rag_num',default=40, type=int)
    parser.add_argument('--api_url',default='https://api.openai.com/v1/chat/completions', type=str)
    parser.add_argument('--api_key',default='', type=str)
    parser.add_argument('--db_path',default='./database', type=str)
    parser.add_argument('--embedding_model',default='nomic-ai/nomic-embed-text-v1', type=str)
    args = parser.parse_args()
    return args

def main(args):
    db = database(db_path = args.db_path, embedding_model = args.embedding_model)
    if not os.path.exists(args.saving_path): os.mkdir(args.saving_path)

    json_files = glob.glob(os.path.join(args.tree_dir, '*_tree.json'))
    if not json_files and args.topic:

        print(f"Warning: No tree files found in {args.tree_dir}, generating from scratch based on topic.")

    
    for json_file in json_files:
        try:
            base_name = os.path.basename(json_file)
            topic_name = base_name.replace('_tree.json', '')
            md_file = json_file.replace('.json', '.md')
            
            with open(md_file, 'r', encoding='utf-8') as f: prior_md = f.read()
            with open(json_file, 'r', encoding='utf-8') as f: prior_json = f.read()

            print(f"=== Processing Topic: {topic_name} ===")

            print("Step 1: Drafting Outline...")
            outline_with_desc, _ = write_outline(
                topic_name, args.model, args.section_num, args.outline_reference_num, 
                db, args.api_key, args.api_url, prior_md, prior_json
            )
            print("Step 2: Writing Content & Generating Tables...")
            results = write_subsection(
                topic_name, args.model, outline_with_desc, args.subsection_len, args.rag_num, 
                db, args.api_key, args.api_url, refinement=True,
                prior_md_content=prior_md, prior_json_content=prior_json
            )
            
            final_md = results[1] 
            final_refs = results[2]

            save_md = os.path.join(args.saving_path, f'{topic_name}.md')
            save_json = os.path.join(args.saving_path, f'{topic_name}.json')
            
            with open(save_md, 'w', encoding='utf-8') as f: f.write(final_md)
            with open(save_json, 'w', encoding='utf-8') as f: 
                json.dump({'survey': final_md, 'reference': final_refs}, f, indent=4)
            
            print(f"=== Done! Saved to {save_md} ===")

        except Exception as e:
            print(f"Error processing {json_file}: {e}")
            import traceback; traceback.print_exc()

if __name__ == '__main__':
    args = paras_args()
    main(args)