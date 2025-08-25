import os
import platform
import redis
from fastapi import HTTPException
from app.config import redis_client

class CoreService:
    def __init__(self):
        self.app_name = "Simple FastAPI Application"
        self.app_version = "1.0.0"
    
    async def health_check(self):
        try:
            # Simple health check implementation
            redis_client.ping()
            return {"status": "healthy", "message": "Application is running correctly", "redis_status": "connected"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    async def get_app_info(self):
        try:
            # Return basic application information
            return {
                "name": self.app_name,
                "version": self.app_version,
                "environment": os.getenv("ENVIRONMENT", "development"),
                "python_version": platform.python_version(),
                "system": platform.system()
            }
        except redis.exceptions.ConnectionError as e:
            raise HTTPException(status_code=500, detail=f"Redis connection failed: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))