import logging
from fastapi import APIRouter, Query, Depends, Request
from app.job.services import JobSearchService, JobRecommendService, JobAddService
from pydantic import BaseModel
from app.core.middleware import verify_api_key

logger = logging.getLogger(__name__)

router = APIRouter()

class Job(BaseModel):
    description: str

@router.post("/add", dependencies=[Depends(verify_api_key)])
async def add_job(request: Request, job: Job):
    logger.info(f"Received add job request: {job.dict()}")
    data = await request.json()
    response = JobAddService(data).add()
    logger.info(f"Add job response: {response}")
    return response

@router.get("/search", dependencies=[Depends(verify_api_key)])
async def search_job(query: str, limit: int = 3):
    logger.info(f"Received search job request: query={query}, limit={limit}")
    response = JobSearchService().search(query, limit)
    logger.info(f"Search job response: {response}")
    return response  

@router.get("/recommend", dependencies=[Depends(verify_api_key)])
async def recommend_job(user_id: str = Query(..., description="The ID of the user")):
    logger.info(f"Received recommend job request for user_id: {user_id}")
    response = JobRecommendService(user_id).recommend()
    logger.info(f"Recommend job response: {response}")
    return response