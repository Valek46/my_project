# routers/books.py

from fastapi import APIRouter, HTTPException, Depends
from dependencies.security import verify_token
from schemas.book_schema import Book
from typing import List

router = APIRouter()

books_db: List[Book] = []

#Авторизация пользователя
@router.get("/books/secure")
async def get_secure_books(token: str = Depends(verify_token)):
    return {"message": "Доступ разрешён к защищённым данным", "token": token}

#Просмотр всех книг
@router.get("/books", response_model=List[Book])
def get_books():
    return books_db

#Поиск по автору
@router.get("/books/search")
def search_books(author: str):
    result = [book for book in books_db if author.lower() in book.author.name.lower()]
    return result

#Просмотр книги по ID
@router.get("/books/{book_id}", response_model=Book)
def get_one_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

#Добавление книги
@router.post("/books/add")
def post_book(book: Book):
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Книга с таким ID уже существует")
    books_db.append(book)
    return {"message": f"Книга '{book.title}' от автора '{book.author.name}' успешно добавлена"}

#Обновление книги
@router.put("/books/{book_id}")
def update_book(book_id: int, new_book: Book):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            if new_book.id != book_id:
                raise HTTPException(status_code=400, detail="ID книги не может быть изменён")
            else:
                books_db[i] = new_book
                return {"message": "Книга обновлена"}
    raise HTTPException(status_code=404, detail="Книга не найдена")

#Удаление книги
@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(i)
            return {"message": "Книга удалена"}
    raise HTTPException(status_code=404, detail="Книга не найдена")
