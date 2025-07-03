from fastapi import Header, HTTPException

async def verify_token(x_token: str = Header(...)):
    if x_token != "secrettoken123":
        raise HTTPException(status_code=401, detail="Недействительный токен")
    return x_token