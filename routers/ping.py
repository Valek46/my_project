# ping.py (оставить только это, если используется)
from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/ping")
async def ping(request: Request):
    return {"message": "pong!"}