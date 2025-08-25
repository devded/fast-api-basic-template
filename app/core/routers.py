from fastapi import APIRouter
from .services import CoreService

router = APIRouter()
service = CoreService()

@router.get("/health", operation_id="health_check")
async def health_check():
    return await service.health_check()

@router.get("/info", operation_id="get_app_info")
async def get_app_info():
    return await service.get_app_info()