# schemas/book_schema.py

from pydantic import BaseModel, Field
from typing import Optional

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=3, max_length=50)
    year: Optional[int] = Field(default=None, ge=1450, le=2025)
    description: Optional[str] = Field(default="Нет описания", max_length=500)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Преступление и наказание",
                "author": "Ф.М. Достоевский",
                "year": 1866,
                "description": "Роман Ф. М. Достоевского о внутренней борьбе человека."
            }
        }

class BookRead(BookCreate):
    id: int = Field(..., ge=0)

    class Config:
        from_attributes = True