from datetime import datetime


class Chat:
    collection_name = "chat_history"

    @staticmethod
    def create(
        user_id: str,
        question: str,
        answer: str,
    ):
        return {
            "user_id": user_id,
            "question": question,
            "answer": answer,
            "created_at": datetime.utcnow(),
        }