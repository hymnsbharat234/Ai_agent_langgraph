from fastapi import APIRouter, Depends, HTTPException
from app.schemes.auth import LoginRequest
from app.schemes.user import UserCreate

from app.services.auth_service import AuthService

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
services=AuthService()

@router.post("/register")
def register(user:UserCreate):
    return services.register(
        user.name,
        user.email,
        user.password
    )
@router.post("/login")
def login(data:LoginRequest):
    return services.login(
        data.email,
        data.password
    )
