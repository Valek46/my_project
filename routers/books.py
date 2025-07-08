from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from dependencies.db import get_session
from models.book_models import Book
from schemas.book_schema import BookCreate, BookRead

router = APIRouter()

@router.post("/books/", response_model=BookRead)
async def create_book(book: BookCreate, session: AsyncSession = Depends(get_session)):
    stmt = insert(Book).values(**book.dict()).returning(Book)
    result = await session.execute(stmt)
    await session.commit()
    created_book = result.scalar_one()
    return created_book
