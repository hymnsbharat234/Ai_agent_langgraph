from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.file_services import file_services
from app.services.rag_services import rag_service
from app.utils.file_utils import validate_file

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    try:
        validate_file(file.filename)

        result = await file_services.save_file(file)

        chunks = rag_service.ingest(result["filepath"])

        result["chunks"] = chunks

        return {
            "success": True,
            "data": result,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )