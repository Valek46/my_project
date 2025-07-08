from sqlalchemy.orm import Mapped, mapped_column
from dependencies.db import Base  # импорт служебного Base

class Book(Base):  # ← вот модель таблицы
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)