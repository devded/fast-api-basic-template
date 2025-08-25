from fastapi import APIRouter
from app.job.services import JobService
from pydantic import BaseModel

router = APIRouter()

class Job(BaseModel):
    description: str

@router.post("/add")
async def add_job(job: Job):
    return JobService().add_job(job.description)

@router.get("/search")
async def search_job(query: str, limit: int = 3):
    return JobService().search_job(query, limit)
