from typing import TypedDict

class GraphState(TypedDict):
    question: str
    route: str
    retrieved_docs: str
    answer: str