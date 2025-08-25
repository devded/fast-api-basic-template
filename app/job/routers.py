from fastapi import APIRouter, Query, Depends
from app.job.services import JobSearchService, JobRecommendService, JobAddService
from pydantic import BaseModel
from app.core.middleware import verify_api_key

router = APIRouter()

class Job(BaseModel):
    description: str

@router.post("/add", dependencies=[Depends(verify_api_key)])
async def add_job(job: Job):
    data = await request.json()
    return JobAddService(data).add()

@router.get("/search", dependencies=[Depends(verify_api_key)])
async def search_job(query: str, limit: int = 3):
    return JobSearchService().search(query, limit)  

@router.get("/recommend", dependencies=[Depends(verify_api_key)])
async def recommend_job(user_id: str = Query(..., description="The ID of the user")):
    return JobRecommendService(user_id).recommend()