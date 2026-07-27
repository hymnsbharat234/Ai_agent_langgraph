from pathlib import Path
from uuid import uuid4

import aiofiles
from fastapi import UploadFile
UPLOAD_DIR=Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

class FileService:
    async def save_file(
            self,
            file:UploadFile
    ):
        extension=Path(file.filename).suffix
        filename=f"{uuid4()}{extension}"

        filepath=UPLOAD_DIR/filename

        async with aiofiles.open(filepath,"wb") as out_file:
            content= await file.read()

            await out_file.write(content)

            return {
                "filename":filename,
                "original_name":file.filename,
                "filepath":str(filepath)
            }

file_services=FileService()