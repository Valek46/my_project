from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator

# 📌 URL для SQLite (в асинхронном режиме)
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# 🔧 Создание движка
engine = create_async_engine(DATABASE_URL, echo=True)

# 🛠️ Создание фабрики сессий
async_session = async_sessionmaker(engine, expire_on_commit=False)

# 🧱 Базовый класс моделей
class Base(DeclarativeBase):
    pass


# ⚙️ Зависимость — получить сессию
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
