from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel

class User:
    collection_name = "users"

    @staticmethod
    def create_user(
        name: str,
        email: str,
        hashed_password: str,
    ):
        return{
            "name": name,
            "email": email,
            "hashed_password": hashed_password,
            "created_at": datetime.utcnow(),
        }