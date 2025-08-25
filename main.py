from fastapi import FastAPI

from app.core.routers import router as core_router

from app.user.routers import router as user_router
from app.job.routers import router as job_router

app = FastAPI(
    title="SimpleAPI",
    description="A simple FastAPI application with core and subscription functionality.",
    version="1.0.0",
)

app.include_router(core_router, prefix="/core", tags=["Core"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(job_router, prefix="/job", tags=["Job"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
