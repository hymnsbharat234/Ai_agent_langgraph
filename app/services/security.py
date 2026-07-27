from datetime import datetime, timedelta
from typing import Optional

from bson import ObjectId
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config.settings import settings
from app.database.database import get_database
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def _normalize_password(password: str) -> str:
    if not password:
        return password

    encoded = password.encode("utf-8")
    if len(encoded) > 72:
        return encoded[:72].decode("utf-8", errors="ignore")
    return password


def hash_password(password: str) -> str:
    return pwd_context.hash(_normalize_password(password))


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(_normalize_password(password), hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECERET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token:str)->Optional[dict]:
    try:
        payload=jwt.decode(token,settings.SECERET_KEY,algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

    db = get_database()
    user = db[User.collection_name].find_one({"_id": ObjectId(user_id)})

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    user["id"] = str(user["_id"])
    del user["_id"]
    del user["hashed_password"]

    return user

