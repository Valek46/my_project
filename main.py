from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers import books, ping
from utils.fake_db import FakeDatabase
from contextlib import asynccontextmanager
import time

# Lifespan: запуск и остановка
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = FakeDatabase()          # ✅ кладём в app.state
    await app.state.db.connect()
    yield
    await app.state.db.disconnect()

app = FastAPI(lifespan=lifespan)

#подключение роутеров
app.include_router(books.router)
app.include_router(ping.router)


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

#Обработчик ошибки
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Ошибка валидации",
            "details": exc.errors()
        }
    )
