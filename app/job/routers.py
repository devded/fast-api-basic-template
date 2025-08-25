from fastapi import APIRouter
from app.job.services import JobSearchService, JobRecommendService, JobAddService
from pydantic import BaseModel

router = APIRouter()

class Job(BaseModel):
    description: str

@router.post("/add")
async def add_job(job: Job):
    data = await request.json()
    return JobAddService(data).add()

@router.get("/search")
async def search_job(query: str, limit: int = 3):
    return JobSearchService().search(query, limit)  

@router.get("/recommend")
async def recommend_job(user_id: str = Query(..., description="The ID of the user")):
    return JobRecommendService(user_id).recommend()