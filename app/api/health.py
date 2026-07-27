from fastapi import APIRouter
from app.database.database import get_database

router=APIRouter(
    prefix="/health",
    tags=["Health Check"]
)

@router.get("/")
async def health_check():
    db=get_database()

    collections=db.list_collection_names()

    return{
        "status":"healthy",
        "database":db.name,
        "collections":collections

    }