from fastapi import APIRouter
from .services import SubscriptionService

router = APIRouter()
service = SubscriptionService()

@router.get("/hello")
async def hello_world():
    return await service.get_hello_world()