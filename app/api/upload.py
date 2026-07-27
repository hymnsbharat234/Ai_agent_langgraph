from fastapi import APIRouter
from  fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile
from app.services.file_services import file_services
from app.utils.file_utils import validate_file

router=APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

@router.post("/")
async def upload_document(
    file:UploadFile=File(...)
):
    try:
        validate_file(file.filename)
        result=await file_services.save_file(file)
        return{
            "success":True
        }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )