
CRITERIA_BASED_JUDGING_PROMPT  = '''
Here is an academic survey about the topic "[TOPIC]":
---
[SURVEY]
---

<instruction>
Please evaluate this survey about the topic "[TOPIC]" based on the criterion above provided below, and give a score from 1 to 5 according to the score description:
---
Criterion Description: [Criterion Description]
---
Score 1 Description: [Score 1 Description]
Score 2 Description: [Score 2 Description]
Score 3 Description: [Score 3 Description]
Score 4 Description: [Score 4 Description]
Score 5 Description: [Score 5 Description]
---
Return the score without any other information:
'''

NLI_PROMPT = '''
---
Claim:
[CLAIM]
---
Source: 
[SOURCE]
---
Claim:
[CLAIM]
---
Is the Claim faithful to the Source? 
A Claim is faithful to the Source if the core part in the Claim can be supported by the Source.\n
Only reply with 'Yes' or 'No':
'''

ROUGH_OUTLINE_PROMPT = '''
You wants to write a overall and comprehensive academic survey about "[TOPIC]".\n\
You are provided with a list of papers related to the topic below:\n\
---
[PAPER LIST]
---
You need to draft a outline based on the given papers.
The outline should contains a title and several sections.
Each section follows with a brief sentence to describe what to write in this section.
The outline is supposed to be comprehensive and contains [SECTION NUM] sections.

Return in the format:
<format>
Title: [TITLE OF THE SURVEY]
Section 1: [NAME OF SECTION 1]
Description 1: [DESCRIPTION OF SENTCTION 1]

Section 2: [NAME OF SECTION 2]
Description 2: [DESCRIPTION OF SENTCTION 2]

...

Section K: [NAME OF SECTION K]
Description K: [DESCRIPTION OF SENTCTION K]
</format>
The outline:
'''


MERGING_OUTLINE_PROMPT = '''
You are an expert in artificial intelligence who wants to write a overall survey about [TOPIC].\n\
You are provided with a list of outlines as candidates below:\n\
---
[OUTLINE LIST]
---
Each outline contains a title and several sections.
Each section follows with a brief sentence to describe what to write in this section.
You need to generate a final outline based on these provided outlines to make the final outline show comprehensive insights of the topic and more logical.
Return the in the format:
<format>
Title: [TITLE OF THE SURVEY]
Section 1: [NAME OF SECTION 1]
Description 1: [DESCRIPTION OF SENTCTION 1]

Section 2: [NAME OF SECTION 2]
Description 2: [DESCRIPTION OF SENTCTION 2]

...

Section K: [NAME OF SECTION K]
Description K: [DESCRIPTION OF SENTCTION K]
</format>
Only return the final outline without any other informations:
'''

SUBSECTION_OUTLINE_PROMPT = '''
You are an expert in artificial intelligence who wants to write an academic survey about "[TOPIC]".

Here is the overall outline:
---
[OVERALL OUTLINE]
---

You need to enrich the section [SECTION NAME].
Description of [SECTION NAME]: [SECTION DESCRIPTION]

Now generate several subsections (3–5 recommended).  
⚠️ Strictly follow this format:

<format>
Subsection 1: [SUBSECTION TITLE]
Description 1: [SUBSECTION DESCRIPTION]

Subsection 2: [SUBSECTION TITLE]
Description 2: [SUBSECTION DESCRIPTION]

Subsection 3: [SUBSECTION TITLE]
Description 3: [SUBSECTION DESCRIPTION]
</format>

Requirements:
- Use the exact prefix "Subsection X:" and "Description X:".
- Do not use "###", "-", or any other formatting.
- Only return the content inside <format>, nothing else.
'''


EDIT_FINAL_OUTLINE_PROMPT = '''
You are an expert in artificial intelligence who wants to write a overall survey about [TOPIC].\n\
You have created a draft outline below:\n\
---
[OVERALL OUTLINE]
---
The outline contains a title and several sections.\n\
Each section follows with a brief sentence to describe what to write in this section.\n\n\
Under each section, there are several subsections.
Each subsection also follows with a brief sentence of descripition.
Some of the subsections may be repeated or overlaped.
You need to modify the outline to make it both comprehensive and logically coherent with no repeated subsections.
Repeated subsections among sections are not allowed!
Return the final outline in the format:
<format>
# [TITLE OF SURVEY]

## [NAME OF SECTION 1]
Description: [DESCRIPTION OF SECTION 1]
### [NAME OF SUBSECTION 1]
Description: [DESCRIPTION OF SUBSECTION 1]
### [NAME OF SUBSECTION 2]
Description: [DESCRIPTION OF SUBSECTION 2]
...

### [NAME OF SUBSECTION L]
Description: [DESCRIPTION OF SUBSECTION L]
## [NAME OF SECTION 2]

...

## [NAME OF SECTION K]
...

</format>
Only return the final outline without any other informations:
'''

CHECK_CITATION_PROMPT = '''
You are an expert in artificial intelligence who wants to write a overall and comprehensive survey about [TOPIC].\n\
Below are a list of papers for references:
---
[PAPER LIST]
---
You have written a subsection below:\n\
---
[SUBSECTION]
---
<instruction>
The sentences that are based on specific papers above are followed with the citation of "paper_title" in "[]".
For example 'the emergence of large language models (LLMs) [Language models are few-shot learners; Language models are unsupervised multitask learners; PaLM: Scaling language modeling with pathways]'

Here's a concise guideline for when to cite papers in a survey:
---
1. Summarizing Research: Cite sources when summarizing the existing literature.
2. Using Specific Concepts or Data: Provide citations when discussing specific theories, models, or data.
3. Comparing Findings: Cite relevant studies when comparing or contrasting different findings.
4. Highlighting Research Gaps: Cite previous research when pointing out gaps your survey addresses.
5. Using Established Methods: Cite the creators of methodologies you employ in your survey.
6. Supporting Arguments: Cite sources that back up your conclusions and arguments.
7. Suggesting Future Research: Reference studies related to proposed future research directions.
---

Now you need to check whether the citations of "paper_title" in this subsection is correct.
A correct citation means that, the content of corresponding paper can support the sentences you write.
Once the citation can not support the sentence you write, correct the paper_title in '[]' or just remove it.

Remember that you can only cite the 'paper_title' provided above!!!
Any other informations like authors are not allowed cited!!!
Do not change any other things except the citations!!!
</instruction>
Only return the subsection with correct citations:
'''

SUBSECTION_WRITING_PROMPT = '''
You are an expert in artificial intelligence who wants to write a overall and comprehensive survey about [TOPIC].\n\
You have created a overall outline below:\n\
---
[OVERALL OUTLINE]
---
Below are a list of papers for references:
---
[PAPER LIST]
---

<instruction>
Now you need to write the content for the subsection:
"[SUBSECTION NAME]" under the section: "[SECTION NAME]"
The details of what to write in this subsection called [SUBSECTION NAME] is in this descripition:
---
[DESCRIPTION]
---

Here is the requirement you must follow:
1. The content you write must be more than [WORD NUM] words.
2. When writing sentences that are based on specific papers above, you cite the "paper_title" in a '[]' format to support your content. An example of citation: 'the emergence of large language models (LLMs) [Language models are few-shot learners; PaLM: Scaling language modeling with pathways]'
    Note that the "paper_title" is not allowed to appear without a '[]' format. Once you mention the 'paper_title', it must be included in '[]'. Papers not existing above are not allowed to cite!!!
    Remember that you can only cite the paper provided above and only cite the "paper_title"!!!
3. Only when the main part of the paper support your claims, you cite it.


Here's a concise guideline for when to cite papers in a survey:
---
1. Summarizing Research: Cite sources when summarizing the existing literature.
2. Using Specific Concepts or Data: Provide citations when discussing specific theories, models, or data.
3. Comparing Findings: Cite relevant studies when comparing or contrasting different findings.
4. Highlighting Research Gaps: Cite previous research when pointing out gaps your survey addresses.
5. Using Established Methods: Cite the creators of methodologies you employ in your survey.
6. Supporting Arguments: Cite sources that back up your conclusions and arguments.
7. Suggesting Future Research: Reference studies related to proposed future research directions.
---

</instruction>
Return the content of subsection "[SUBSECTION NAME]" in the format:
<format>
[CONTENT OF SUBSECTION]
</format>
Only return the content more than [WORD NUM] words you write for the subsection [SUBSECTION NAME] without any other information:
'''


LCE_PROMPT = '''
You are an expert in artificial intelligence who wants to write a overall and comprehensive survey about [TOPIC].

Now you need to help to refine one of the subsection to improve th ecoherence of your survey.

You are provied with the content of the subsection along with the previous subsections and following subsections.

Previous Subsection:
--- 
[PREVIOUS]
---

Following Subsection:
---
[FOLLOWING]
---

Subsection to Refine: 
---
[SUBSECTION]
---


If the content of Previous Subsection is empty, it means that the subsection to refine is the first subsection.
If the content of Following Subsection is empty, it means that the subsection to refine is the last subsection.

Now refine the subsection to enhance coherence, and ensure that the content of the subsection flow more smoothly with the previous and following subsections. 

Remember that keep all the essence and core information of the subsection intact. Do not modify any citations in [] following the sentences.

Only return the whole refined content of the subsection without any other informations (like "Here is the refined subsection:")!

The subsection content:
'''


TREE_PROMPT = """
You are an expert in artificial intelligence tasked with producing a clean, comprehensive tree diagram about the topic: [TOPIC]. Output must be in ENGLISH.

PAPER LIST
[PAPER LIST]

GOALS
- Produce a 3-level tree: Title → Section → Subsection → Keyword.
- For each Subsection, list 1-4 short keywords (1-3 words each), no extra prose.
- Each keyword must cite at least three retrieved paper using the format [RID:paper_id], where paper_id is EXACTLY one of the IDs provided in PAPER LIST (e.g., 1811.06122v1).
- Multiple citations are strongly encouraged (2-3 per keyword when possible), e.g. [RID:1811.06122v1][RID:1811.06115v1].
- You MUST actively distribute citations across as many DIFFERENT [RID] values as possible to maximize coverage of PAPER LIST. 
- Reuse of the same [RID:paper_id] across different nodes should happen only if it is *essentially relevant*. Excessive repetition of the same IDs will be considered an error.
- If no suitable paper exists, leave the keyword WITHOUT citation rather than fabricating or repeating irrelevant IDs.


FORMATTING (exact ASCII; return ONE fenced code block and nothing else)
- Keep vertical bars `|` aligned exactly as shown; do not add extra commentary.
- Use these exact prefixes:
  1) `|----Section X: [Title]`
  2) `|     |----Subsection X.X: [Title]`
  3) `|     |     |----keyword: [RID:paper_id]`
- Do NOT write the word “Keywords”; just place the keyword text and citations.
- Title line is the very first line (no prefix).

OUTPUT TEMPLATE
title
|----Section 1: [Title]
|     |----Subsection 1.1: [Title]
|     |     |----keyword1: [RID:1811.06122v1][RID:1811.06115v1]
|     |     |----keyword2: [RID:1811.06114v2]
|----Section 2: [Title]
......

The system will generate references later using PAPER LIST.
"""

