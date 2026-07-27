from app.services.llm import llm


def answer_agent(state):

    history = ""
    history_items = state.get("history", [])

    for chat in history_items:
        if isinstance(chat, dict):
            user_text = chat.get("question") or chat.get("content", "")
            assistant_text = chat.get("answer") or chat.get("content", "")
        else:
            user_text = str(chat)
            assistant_text = ""

        history += f"""

User:
{user_text}

Assistant:
{assistant_text}
"""

    prompt = f"""
You are an AI Research Assistant.

Conversation History:

{history}

Question:

{state['question']}

Context:

{state['retrieved_docs']}

Answer naturally.
"""

    response = llm.invoke(prompt)

    state["answer"] = response.content
    state.setdefault("history", [])
    state["history"].append({
        "question": state["question"],
        "answer": state["answer"],
    })

    return state