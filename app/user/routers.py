from fastapi import APIRouter, Depends, Request
from app.user.services import UserAddService
from app.core.middleware import verify_api_key

router = APIRouter()

@router.post("/add", dependencies=[Depends(verify_api_key)])
async def add_user(request: Request):
    data = await request.json()
    return UserAddService(data=data).add()

