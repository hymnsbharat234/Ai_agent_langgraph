from typing import TypedDict

class GraphState(TypedDict):
    question: str
    route: str
    retrieved_docs: str
    answer: str
    history: list
    user_id: str | None