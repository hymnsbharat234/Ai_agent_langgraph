from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.builder import graph

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "question": request.question,
            "retrieved_docs": "",
            "answer": "",
        }
    )

    return {
        "question": result["question"],
        "answer": result["answer"],
    }