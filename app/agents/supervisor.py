from app.services.llm import llm


def supervisor(state):

    prompt = f"""
You are a supervisor agent.

Choose ONLY one route.

Return exactly one word.

rag
web
general

Question:
{state["question"]}
"""

    response = llm.invoke(prompt)

    state["route"] = response.content.strip().lower()

    return state
