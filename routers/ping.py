from fastapi import APIRouter, Depends
from dependencies.db import get_db

router = APIRouter()

@router.get("/ping")
async def ping(db = Depends(get_db)):
    status = "подключено" if db.connected else "не подключено"
    return {"db_status": status}
