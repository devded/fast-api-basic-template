from fastapi import APIRouter
from app.job.services import JobAddService, JobSearchService

router = APIRouter()

@router.post("/add")
async def add_job():
    return JobAddService().add()

@router.get("/search")
async def search_job():
    return JobSearchService().search()
