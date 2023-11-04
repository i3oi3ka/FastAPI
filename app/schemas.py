from datetime import datetime

from pydantic import BaseModel


# class Employee(BaseModel):
#     id: int
#     first_name: str
#     last_name: str
#     date_joined: datetime.date
#     age: int
#     city: str
#     library_id: int
#     is_active: bool
#     salary: int


class BaseBook(BaseModel):
    title: str
    description: str | None = None
    published_year: int
    price: int
    author_id: int


class CreateBook(BaseBook):
    pass


class Book(BaseBook):
    id: int

    class Config:
        orm_mode = True


class BaseAuthor(BaseModel):
    first_name: str
    last_name: str


class CreateAuthor(BaseAuthor):
    pass


class Author(BaseAuthor):
    id: int

    class Config:
        orm_mode = True

# class Book(BaseModel):
#     id: int
#     title: str
#     description: str | None = None
#     author: str
#     published_year: int
#     # libraries: List[str]
#     # another: AnotherModel
#     price: int
#
#
# class BookWithPrice(Book):
#     price: int
