# schemas/book_schema.py

from pydantic import BaseModel, Field
from typing import Optional

class Author(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    birth_year: int = Field(ge=1000, le=2025)

class Book(BaseModel):
    id: int = Field(ge=0)
    title: str
    description: Optional[str] = Field(default="Нет описания", max_length=500)
    year: int = Field(ge=1450, le=2025)
    author: Author

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Преступление и наказание",
                "description": "Роман Ф. М. Достоевского о внутренней борьбе человека.",
                "year": 1866,
                "author": {
                    "name": "Ф.М. Достоевский",
                    "birth_year": 1821
                }
            }
        }
