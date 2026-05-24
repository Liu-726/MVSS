# src/agents/feedback_utils.py

def build_feedback_instructions(scores, criteria, threshold=4):
    """
    根据 judge 的分数生成改进指令
    scores: [3, 2, 5, 3]  (对应 Coverage, Structure, Relevance, Salience Alignment)
    criteria: ["Coverage", "Structure", "Relevance", "Salience Alignment"]
    """
    feedbacks = []
    for score, crit in zip(scores, criteria):
        if score < threshold:
            if crit == "Coverage":
                feedbacks.append(
                    "- Coverage is insufficient: expand by including missing subtopics and incorporating more diverse references."
                )
            elif crit == "Structure":
                feedbacks.append(
                    "- Structure needs improvement: reorganize the tree to ensure logical and balanced sections, avoiding redundancy."
                )
            elif crit == "Relevance":
                feedbacks.append(
                    "- Relevance is weak: filter out unrelated keywords and ensure all nodes are tightly aligned to the topic."
                )
            elif crit == "Salience Alignment":
                feedbacks.append(
                    "- Salience Alignment is low: reorder keywords so that high-frequency and recent research appears earlier."
                )

    if feedbacks:
        return "Please improve the tree diagram according to the following points:\n" + "\n".join(feedbacks)
    else:
        return "No major issues. Keep the structure."