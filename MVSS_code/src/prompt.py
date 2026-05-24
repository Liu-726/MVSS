# src/prompt.py

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

Here is some prior knowledge about the topic. Use this to create a more accurate and structured outline:
---
[PRIOR KNOWLEDGE MD]
---

Here is a prior topic tree structure. Use this as a strong reference for your new outline:
---
[PRIOR KNOWLEDGE JSON]
---

You are provided with a list of papers related to the topic below:\n\
---
[PAPER LIST]
---
You need to draft a outline based on the given papers and the prior knowledge provided.
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
You are an expert in artificial intelligence who wants to write a overall survey about [TOPIC].\n\
You have created a overall outline below:\n\
---
[OVERALL OUTLINE]
---
The outline contains a title and several sections.\n\
Each section follows with a brief sentence to describe what to write in this section.\n\n\

Here is some prior knowledge about the topic. Use this to create a more accurate and structured outline:
---
[PRIOR KNOWLEDGE MD]
---

Here is a prior topic tree structure. Use this as a strong reference for your new outline:
---
[PRIOR KNOWLEDGE JSON]
---

<instruction>
You need to enrich the section [SECTION NAME].
The description of [SECTION NAME]: [SECTION DESCRIPTION]
You need to generate the framwork containing several subsections based on the overall outlines and prior knowledge.\n\
Each subsection follows with a brief sentence to describe what to write in this subsection.
These papers provided for references:
---
[PAPER LIST]
---
Return the outline in the format:
<format>
Subsection 1: [NAME OF SUBSECTION 1]
Description 1: [DESCRIPTION OF SUBSENTCTION 1]

Subsection 2: [NAME OF SUBSECTION 2]
Description 2: [DESCRIPTION OF SUBSENTCTION 2]

...

Subsection K: [NAME OF SUBSECTION K]
Description K: [DESCRIPTION OF SUBSENTCTION K]
</format>
</instruction>
Only return the outline without any other informations:
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
You are an expert in artificial intelligence writing a comprehensive survey on [TOPIC].

**Context Papers (Source Material):**
---
[PAPER_LIST]
---

**Prior Knowledge (Context ONLY, do not reproduce):**
---
[PRIOR KNOWLEDGE MD]
---

**Instruction:**
Write the content for Subsection "[SUBSECTION NAME]" (Section: "[SECTION NAME]").
Description: [DESCRIPTION]

**Strict Constraints:**
1. **Length**: between 500 and 1000 words (hard limit: do not exceed 1000).
2. **NO Repetition**: Do NOT repeat the subsection title (e.g., "### [SUBSECTION NAME]") at the beginning. Start writing the paragraph directly.
3. **NO Tree Output**: Do NOT output the [PRIOR KNOWLEDGE MD] tree.
4. **Citation Format**: 
   - You MUST cite papers using the format `[Paper Title]`. 
   - Example: "...as proposed in [Attention is all you need]."
   - **FORBIDDEN**: Do NOT use `[1]`, `[Author et al]`, or `(Year)`. 
   - Only cite papers provided in the "Context Papers" list.

Output ONLY the subsection content.
'''

LOCAL_TABLE_REFLECT_PROMPT = '''
You are a meticulous academic editor.
**Task**: Create a Markdown comparison table based on the provided text AND source papers.

**Input 1: Written Text**
[SUBSECTION_CONTENT]

**Input 2: Source Papers (Reference List & Details)**
[PAPER_LIST]

**Steps:**
1. **Decision**: Does the text discuss/compare **3 or more** distinct methods/models? 
   - If NO -> Output strictly: "NO_TABLE"
   - If YES -> Generate the table.

**Table Construction Rules (CRITICAL):**
1. **Output Format**: 
   - Output **RAW Markdown** format only.
   - **DO NOT wrap the table in a code block (like ```markdown ... ```).**
   - **Do NOT** output "YES", "Here is the table", "Sure", or any conversational filler.
   - **Do NOT** use ASCII borders (like `+---+`). Use standard Markdown pipes `|`.
   - **Do NOT** use newlines (`\n`) inside a cell. Keep each row on a single line.

2. **Content Source**:
   - Use "Input 1" to identify WHICH methods to compare.
   - Use "Input 2" to fill in DETAILS (Year, Dataset, Backbone) that might be missing in the text.

3. **Citation Format**:
   - The "Reference" column MUST use the **Exact Full Paper Title** from "Input 2".
   - Example: `[Attention is all you need]`
   - **FORBIDDEN**: `[1]`, `[Vaswani]`, `[Link](url)`.

Return ONLY the Markdown table code or "NO_TABLE".
'''