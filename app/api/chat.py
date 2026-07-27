from datetime import datetime

from bson import ObjectId
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from app.graph.builder import graph
from app.services.chat_service import chat_service
from app.services.security import get_current_user, get_current_user_optional

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


def _serialize_history(history):
    if not history:
        return []

    serialized = []
    for item in history:
        if isinstance(item, dict):
            normalized = {}
            for key, value in item.items():
                if key == "_id":
                    continue
                if isinstance(value, ObjectId):
                    normalized[key] = str(value)
                elif isinstance(value, datetime):
                    normalized[key] = value.isoformat()
                elif isinstance(value, dict):
                    normalized[key] = _serialize_history([value])[0]
                elif isinstance(value, list):
                    normalized[key] = [_serialize_history([entry])[0] if isinstance(entry, dict) else entry for entry in value]
                else:
                    normalized[key] = value
            serialized.append(normalized)
        else:
            serialized.append(item)

    return serialized


class ChatRequest(BaseModel):
    question: str
    history: list | None = None
    user_id: str | None = None


@router.post("/")
def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user_optional),
):
    history = request.history or []
    user_id = request.user_id

    if current_user is not None:
        stored_history = chat_service.get_history(current_user["id"])
        history = stored_history + history
        user_id = current_user.get("id") or current_user.get("_id") or user_id

    result = graph.invoke(
        {
            "question": request.question,
            "route": "",
            "retrieved_docs": "",
            "answer": "",
            "history": history,
            "user_id": user_id,
        }
    )

    if result.get("answer"):
        chat_service.save_chat(
            user_id or "anonymous",
            request.question,
            result["answer"],
        )

    if isinstance(result, dict):
        result["history"] = _serialize_history(result.get("history", []))

    return result