from fastapi import HTTPException
from sqlalchemy.orm import Session

from .models import Book, Author
from .schemas import CreateBook, CreateAuthor


# Book CRUD
def book_list(db: Session):
    return db.query(Book).all()


def book_create(db: Session, book: CreateBook):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def book_retrieve(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def book_update(db: Session, book: CreateBook, book_id: int):
    book_model = book_retrieve(db, book_id)
    for key, value in book.model_dump().items():
        setattr(book_model, key, value)
    db.commit()
    return book_model


def book_delete(db: Session, book_id: int):
    book = book_retrieve(db, book_id)
    db.delete(book)
    db.commit()
    return {"message": "Book delete successfully"}


# Author CRUD

def author_create(db: Session, author: CreateAuthor):
    db_author = Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def author_retrieve(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


def author_list(db: Session):
    return db.query(Author).all()


def author_update(db: Session, author_id: int, author: CreateAuthor):
    author_model = author_retrieve(db, author_id)
    for key, value in author.model_dump().items():
        setattr(author_model, key, value)
    db.commit()
    return author_model


def author_delete(db: Session, author_id: int):
    author = author_retrieve(db, author_id)
    db.delete(author)
    db.commit()
    return {"message": "Author delete successfully"}
