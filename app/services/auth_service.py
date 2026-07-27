from bson import ObjectId
from fastapi import HTTPException, status
from app.database.database import get_database

from app.models.user import User
from app.services.security import (
    create_access_token,
    hash_password,
    verify_password
)

class AuthService:
    def __init__(self):
        self.db=get_database()
        self.users=self.db[User.collection_name]


    def register(self,name,email, password):
            if self.users.find_one({"email":email}):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered"
                )
            hashed=hash_password(password)
            user=User.create_user(name,email,hashed)
            result=self.users.insert_one(user)
            return {"id":str(result.inserted_id),
                    "message":"User registered successfully"
            }

    def login(self,email,password):
            user=self.users.find_one({"email":email})
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid email or password"
                )
            if not verify_password(password,user["hashed_password"]):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid email or password"
                )
            token=create_access_token(data={"sub":str(user["_id"]),"email":user["email"]})
            return {"access_token":token,"token_type":"bearer"}