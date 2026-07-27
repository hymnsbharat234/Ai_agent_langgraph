from fastapi import APIRouter,Depends
from app.services.security import get_current_user

router=APIRouter(
    prefix="/users",
    tags=["Users"]

)

@router.get("/me")
def get_profile(current_user=Depends(get_current_user),):
    return current_user