from pydantic import BaseModel, EmailStr
from datetime import datetime

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class tokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int