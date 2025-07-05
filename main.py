from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers import books
from contextlib import asynccontextmanager
from datetime import datetime
import time

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код при запуске
    with open("state.txt", "a", encoding="utf-8") as f:
        f.write(f"🚀 START at {datetime.now()}\n")

    yield  # ⬅️ Переход к обработке запросов

    # Код при завершении
    with open("state.txt", "a", encoding="utf-8") as f:
        f.write(f"🛑 SHUTDOWN at {datetime.now()}\n")

app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def log_request(request: Request, call_next):
    start_time = time.time()

    client_ip = request.client.host
    method = request.method
    url = str(request.url)

    print(f"[{method}] {url} — от {client_ip}")

    response = await call_next(request)

    duration = time.time() - start_time
    print(f"Обработан за {duration:.3f} сек")

    return response

app.include_router(books.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Ошибка валидации",
            "details": exc.errors()
        }
    )
