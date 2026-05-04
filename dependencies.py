# dependencies.py
from fastapi import Header, HTTPException

async def verify_api_key(x_api_key: str = Header(default=None)):
    if x_api_key != "secret-raj-123":
        raise HTTPException(status_code=401, detail="Invalid API Key. Access Denied!")
    return x_api_key