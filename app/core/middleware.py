from fastapi import Request, HTTPException, Header
from typing import Optional

async def verify_api_key(api_key: Optional[str] = Header(None, alias="X-API-Key")):
    # In a real application, this secret would be securely stored and retrieved
    # For demonstration, we'll use a hardcoded secret or environment variable
    expected_secret = "your-super-secret-key"

    if api_key is None or api_key != expected_secret:
        raise HTTPException(status_code=403, detail="Unauthorized: Invalid or missing X-API-Key header")
    return True