from fastapi import APIRouter, Depends, HTTPException
from app.schemes.auth import LoginRequest
from app.schemes.user import UserCreate

from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm

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
def login(form_data:OAuth2PasswordRequestForm=Depends(),):
    return services.login(
        form_data.username,
        form_data.password
    )
