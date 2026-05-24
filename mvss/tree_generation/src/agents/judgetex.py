import threading
import re
from src.model import APIModel
from src.utils import tokenCounter
from src.prompt import CRITERIA_BASED_JUDGING_PROMPT

CRITERIA = {
    'Coverage': {
        'description': 'Coverage: Coverage assesses the extent to which the tree diagram encapsulates all relevant aspects of the topic, ensuring that both central and peripheral areas are represented with appropriate citations.',
        'score 1': 'The tree diagram has very limited coverage, citing only a small fraction of the retrieved papers and omitting most key areas of the topic.',
        'score 2': 'The tree diagram covers some parts of the topic but shows noticeable gaps; several important themes or groups of papers are missing.',
        'score 3': 'The tree diagram provides a reasonable level of coverage, with many important areas represented, but still leaves out a few significant themes or citations.',
        'score 4': 'The tree diagram covers most major aspects of the topic comprehensively, with only minor omissions or underrepresented sub-areas.',
        'score 5': 'The tree diagram achieves comprehensive coverage, including both central and peripheral aspects of the topic, and distributes citations widely across the retrieved papers.'
    },

    'Structure': {
        'description': 'Structure: Structure evaluates the logical organization, clarity, and balance of sections, subsections, and keywords within the tree diagram.',
        'score 1': 'The tree diagram lacks clear organization, with sections and subsections arranged arbitrarily, making the hierarchy hard to follow.',
        'score 2': 'The tree diagram has weak structural coherence; some sections are disordered, unbalanced, or illogically grouped.',
        'score 3': 'The tree diagram has a generally reasonable structure, with most content arranged logically, though some subsections may be repetitive, unbalanced, or loosely connected.',
        'score 4': 'The tree diagram is well-structured, with logical and balanced sections, smooth transitions, and only slight rigidity or redundancy in a few parts.',
        'score 5': 'The tree diagram is tightly organized, logically coherent at all levels, with balanced sections and subsections, and clear hierarchical flow from top to bottom.'
    },

    'Relevance': {
        'description': 'Relevance: Relevance measures how well the keywords and citations in the tree diagram align with the research topic, ensuring that nodes and references are appropriate and meaningful.',
        'score 1': 'The content is largely irrelevant, with keywords and citations unrelated to the topic or misleading in context.',
        'score 2': 'The tree diagram is somewhat relevant but contains multiple digressions; citations or keywords often stray from the core topic.',
        'score 3': 'The tree diagram is generally relevant, with most keywords and citations on topic, though a few nodes or references may not fit well.',
        'score 4': 'The tree diagram is highly relevant and focused, with the vast majority of keywords and citations directly tied to the topic, and only occasional minor misalignments.',
        'score 5': 'The tree diagram is exceptionally relevant, with every keyword and citation tightly aligned to the topic, ensuring clarity, focus, and meaningful contribution throughout.'
    },

    'Salience Alignment': {
        'description': 'Salience Alignment: Salience Alignment assesses whether more important keywords are placed in more prominent positions within each subsection (earlier lines), supporting navigability and user comprehension. Importance can be judged qualitatively (semantic weight) rather than frequency/recency.',
        'score 1': 'The ordering of keywords is highly inconsistent with their importance: trivial items appear early while important ones are buried.',
        'score 2': 'Keyword ordering shows weak alignment; some relevant items are prioritized, but many high-value terms appear late or inconsistently.',
        'score 3': 'Keyword ordering demonstrates moderate alignment: many important keywords appear earlier, though there are noticeable inconsistencies.',
        'score 4': 'Keyword ordering is strongly aligned with importance, with most high-value terms appearing early and only minor local reversals.',
        'score 5': 'Keyword ordering is fully aligned: all major/important keywords are consistently placed in prominent positions, ensuring clarity and efficiency.'
    }
}

class JudgeTex:
    def __init__(self, model: str, api_key: str, api_url: str) -> None:
        self.model = model
        self.api_key = api_key
        self.api_url = api_url
        self.api_model = APIModel(model, api_key, api_url)
        self.token_counter = tokenCounter()
        self.input_token_usage = 0
        self.output_token_usage = 0

    def compute_price(self):
        return self.token_counter.compute_price(
            input_tokens=self.input_token_usage, 
            output_tokens=self.output_token_usage, 
            model=self.model
        )

    def __generate_prompt(self, template, paras):
        prompt = template
        for k, v in paras.items():
            prompt = prompt.replace(f'[{k}]', str(v))
        return prompt

    def extract_num(self, string):
        if not string:
            return 0
        numbers = re.findall(r'\d+', string)
        if len(numbers) == 0:
            return 0
        return int(numbers[0])

    def __criteria_based_judging(self, topic, survey_content, criterion, res_dict, lock):
       
        if criterion not in CRITERIA:
            print(f"[Error] Criterion '{criterion}' not found in configuration.")
            return

        criterion_paras = CRITERIA[criterion]
        
        format_instruction = (
            "\n\n[IMPORTANT INSTRUCTION FOR THE JUDGE]:\n"
            "The content below is provided in raw **LaTeX format**.\n"
            "You must evaluate the **intellectual content, logic, and coverage** only.\n"
            "1. Strictly **IGNORE** all LaTeX syntax (e.g., \\section, \\cite{}, \\begin{}).\n"
            "2. Do **NOT** penalize the score because the text looks like code or unrendered text.\n"
            "3. Focus solely on whether the information provided meets the evaluation criterion.\n"
            "--------------------------------------------------\n"
        )
        
   
        wrapped_content = format_instruction + survey_content

     
        content_paras = {
            'TOPIC': topic, 
            'SURVEY': wrapped_content,  
            'Criterion Description': criterion_paras['description']
        }
        
      
        for score in range(1, 6):
            content_paras[f'Score {score} Description'] = criterion_paras[f'score {score}']

        
        try:
            prompt = self.__generate_prompt(CRITERIA_BASED_JUDGING_PROMPT, content_paras)
            self.input_token_usage += self.token_counter.num_tokens_from_string(prompt)
        except Exception as e:
            print(f"[Error] Failed to generate prompt for {criterion}: {e}")
            return

        print(f"   >>> [Running] Evaluating criterion: {criterion}...") 

        try:
            
            response = self.api_model.chat(prompt, temperature=0)
            
          
            if not response:
                print(f"   !!! [Warning] Empty response from API for {criterion}")
                score = 0
            else:
                score = self.extract_num(response)
                
        except Exception as e:
            print(f"   !!! [Exception] API Call failed for {criterion}: {e}")
            score = 0
            response = f"Error: {str(e)}"

       
        with lock:
            res_dict[criterion] = {
                "score": score,
                "reasoning": response
            }
        
        print(f"   <<< [Done] {criterion} finished. Score: {score}")

    def evaluate_survey(self, topic: str, survey_content: str, criteria_list: list = None):
       
      
        if criteria_list is None:
            criteria_list = ['Coverage', 'Structure', 'Relevance', 'Salience Alignment']

        threads = []
        results = {}
        lock = threading.Lock()

        print(f"Starting evaluation (JudgeTex) for topic: {topic}...")
        print(f"Dimensions: {criteria_list}")

        for criterion in criteria_list:
            t = threading.Thread(
                target=self.__criteria_based_judging, 
                args=(topic, survey_content, criterion, results, lock)
            )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return results