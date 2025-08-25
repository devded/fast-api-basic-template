import logging
from fastapi import APIRouter, Depends, Request
from app.user.services import UserAddService
from app.core.middleware import verify_api_key

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/add", dependencies=[Depends(verify_api_key)])
async def add_user(request: Request):
    data = await request.json()
    logger.info(f"Received add user request: {data}")
    response = UserAddService(data=data).add()
    logger.info(f"Add user response: {response}")
    return response

