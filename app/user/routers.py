from fastapi import APIRouter
from app.user.services import UserAddService

router = APIRouter()

@router.post("/add")
async def add_user(request: Request):
    data = await request.json()
    return UserAddService(data=data).add()

