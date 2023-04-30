from typing import Annotated

from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix='/video', tags=["Video"])


@router.post('/')
async def create_video(file: UploadFile = File()):
    """Загрузить новое видео"""
    return {"file_size": file.filename}
