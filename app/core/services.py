import platform
import os
from fastapi import HTTPException

class CoreService:
    def __init__(self):
        self.app_name = "Simple FastAPI Application"
        self.app_version = "1.0.0"
    
    async def health_check(self):
        try:
            # Simple health check implementation
            return {"status": "healthy", "message": "Application is running correctly"}
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
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))