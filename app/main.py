from typing import List, Annotated

from fastapi import FastAPI, status, Depends, Path
from sqlalchemy.orm import Session

from .crud import book_list, book_create, book_retrieve, book_update, author_create, book_delete, author_retrieve, \
    author_update, author_list, author_delete
from .database import SessionLocal
from .schemas import Book, CreateBook, Author, CreateAuthor


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# class RandomEnum(Enum):
#     one = 'one'
#     two = 'two'
#

app = FastAPI()
employee_data = []


@app.get("/books/")
async def get_book_list(db: Session = Depends(get_db)) -> List[Book]:
    books = book_list(db)
    return books


@app.get("/books/{book_id}")
async def get_book(
        book_id: Annotated[int, Path(title="Id for book in my store", ge=1)],
        db: Session = Depends(get_db)) -> Book:
    book = book_retrieve(db, book_id)
    return book


@app.post("/books/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(
        book: CreateBook,
        db: Session = Depends(get_db)) -> Book:
    return book_create(db, book)


@app.put("/books/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(
        book_id: Annotated[int, Path(ge=1)],
        book: CreateBook,
        db: Session = Depends(get_db)
) -> Book:
    return book_update(db, book, book_id)


@app.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(
        book_id: Annotated[int, Path(ge=1)],
        db: Session = Depends(get_db)
) -> dict:
    return book_delete(db, book_id)


# Author CRUD
@app.post("/author/", response_model=Author, status_code=status.HTTP_201_CREATED)
async def create_author(
        author: CreateAuthor,
        db: Session = Depends(get_db)
) -> Author:
    return author_create(db, author)


@app.get("/authors/{author_id}", status_code=status.HTTP_200_OK)
async def get_author(
        author_id: Annotated[int, Path(ge=1)],
        db: Session = Depends(get_db)
) -> Author:
    return author_retrieve(db, author_id)


@app.get("/authors/", status_code=status.HTTP_200_OK)
async def get_author_list(
        db: Session = Depends(get_db)
) -> List[Author]:
    return author_list(db)


@app.put("/authors/{author_id}", response_model=Author, status_code=status.HTTP_200_OK)
async def update_author(
        author_id: Annotated[int, Path(ge=1)],
        author: CreateAuthor,
        db: Session = Depends(get_db)
) -> Author:
    return author_update(db, author_id, author)


@app.delete("/authors/{author_id}", status_code=status.HTTP_200_OK)
async def delete_author(
        author_id: Annotated[int, Path(ge=1)],
        db: Session = Depends(get_db)
) -> dict:
    return author_delete(db, author_id)
# @app.get("/books/")
# async def get_book_list(q: Annotated[list[str] | None, Query(min_length=5, max_length=10, pattern=r'^search_.*')] = ['1','2','3','4','5'] , is_active: bool = False):
#     # if pricegt is not None:
#     #     books = list(filter(lambda x: x['price'] > pricegt, books_data))
#     #     return {"books": books, "is_active": is_active}
#
#     return {"books": books_data, "is_active": is_active, "q": q}

# #Cookie
# @app.get("/books/")
# async def get_book_list(q: Annotated[str | None, Query()] = None, my_cookies: Annotated[str | None, Cookie()] = None):
#     return {"books": books_data, "q": q, "my_cookies": my_cookies}
#
# #Header
# @app.get("/books/")
# async def get_book_list(q: Annotated[str | None, Query()] = None, content_type: Annotated[str | None, Header()] = None):
#     return {"books": books_data, "q": q, "content_type": content_type}


# @app.get("/books/{book_id}")
# async def get_book(book_id: int, limit: int | None = None):
#     book = list(filter(lambda x: x['id'] == book_id, books_data))[0]
#     book['limit'] = limit
#     return book

# @app.get("/books/{book_id}")
# async def get_book(book_id: Annotated[int, Path(ge=1, title='ID for book in my store')], q: str):
#     book = list(filter(lambda x: x['id'] == book_id, book_data))[0]
#
#     return book


# @app.post("/books/{book_id}", response_model=Book)
# async def create_book(book: BookWithPrice) -> Book:
#     return book

# Response

#
# @app.post("/books/{book_id}")
# async def create_book(book: BookWithPrice) -> JSONResponse:
#     return JSONResponse(content= {**book.model_dump()})


# status code
# @app.post("/books/{book_id}", response_model=Book, status_code=status.HTTP_201_CREATED)
# async def create_book(book: Book):
#     return book


# # 2. Для отриманн списку користувачів додайте 3 query параметри за якими буде відбуватись фільтрація даних!
# @app.get("/employee/")
# async def get_employee(
#         id: Annotated[int | None, Query()] = None,
#         library_id: Annotated[int | None, Query()] = None,
#         first_name: Annotated[str | None, Query(min_length=3, max_length=15)] = None
# ):
#     if id:
#         employees = next((employee for employee in employee_data if employee.id == id), None)
#         if employees is None:
#             raise HTTPException(status_code=404, detail="Employee not found")
#     if library_id:
#         employees = list(filter(lambda x: x.library_id == library_id, employee_data))
#     if first_name:
#         employees = list(filter(lambda x: x.first_name == first_name, employee_data))
#     return employees
#
#
# @app.post("/employee/", response_model=Employee, status_code=status.HTTP_201_CREATED)
# async def create_employee(employee: Employee) -> Employee:
#     employee_data.append(employee)
#     return employee
#
#
# @app.put("/employee/", response_model=Employee, status_code=200)
# async def update_employee(employee_id: int, update_employee: Employee) -> Employee:
#     employee = next((employee for employee in employee_data if employee.id == employee_id), None)
#     if employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     employee.first_name = update_employee.first_name
#     employee.last_name = update_employee.last_name
#     employee.date_joined = update_employee.date_joined
#     employee.age = update_employee.age
#     employee.city = update_employee.city
#     employee.library_id = update_employee.library_id
#     employee.is_active = update_employee.is_active
#     employee.salary = update_employee.salary
#     return employee
