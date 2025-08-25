from fastapi import FastAPI
from app.core.routers import router as core_router
from app.subscription.routers import router as subscription_router

def create_application() -> FastAPI:
    app = FastAPI(title="Basic Fast API", description="API Docs For Basic App")
    
    @app.get("/", tags=["root"])
    async def read_root():
        return {"message": "Welcome to the Basic Fast API"}
    
    # Register routers
    app.include_router(core_router, prefix="/core", tags=["core"])
    app.include_router(subscription_router, prefix="/subscription", tags=["subscription"])
    
    return app

app = create_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
