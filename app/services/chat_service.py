from datetime import datetime

from bson import ObjectId

from app.database.database import get_database
from app.models.chat import Chat


class ChatService:

    def __init__(self):

        db = get_database()

        self.collection = db[Chat.collection_name]

    def _serialize_history_item(self, item):
        if isinstance(item, dict):
            serialized = {}
            for key, value in item.items():
                if key == "_id":
                    continue
                if isinstance(value, ObjectId):
                    serialized[key] = str(value)
                elif isinstance(value, datetime):
                    serialized[key] = value.isoformat()
                elif isinstance(value, dict):
                    serialized[key] = self._serialize_history_item(value)
                elif isinstance(value, list):
                    serialized[key] = [self._serialize_history_item(v) for v in value]
                else:
                    serialized[key] = value
            return serialized

        if isinstance(item, ObjectId):
            return str(item)

        if isinstance(item, datetime):
            return item.isoformat()

        return item

    def save_chat(
        self,
        user_id,
        question,
        answer,
    ):

        self.collection.insert_one(
            Chat.create(
                user_id,
                question,
                answer,
            )
        )

    def get_history(
        self,
        user_id,
        limit=5,
    ):

        history = list(

            self.collection.find(
                {
                    "user_id": user_id
                }
            ).sort(
                "created_at",
                -1,
            ).limit(limit)

        )

        return [self._serialize_history_item(item) for item in history]


chat_service = ChatService()