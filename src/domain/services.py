from dataclasses import dataclass
from typing import Sequence
from domain.entity import Book, StatusEnum
from domain.event import CreateBook, DeleteBook, SetStatusBook
from infrastructure.repository.books.interface import IBookRepository


@dataclass
class ServicesBook:
    repository: IBookRepository

    def add_book(self, title: str, author: str, year: int) -> Book:
        event = CreateBook(title, author, year)
        return self.repository.add(event)

    def delete_book(self, id: int) -> None:
        event = DeleteBook(id=id)
        self.repository.delete(event)

    def search_book(self, query: str) -> Sequence[Book]:
        return self.repository.search(query)

    def get_all_book(self) -> Sequence[Book]:
        return self.repository.all()

    def set_status_book(self, item_id: int, new_status: str) -> None:
        event = SetStatusBook(id=item_id, status=StatusEnum(new_status))
        self.repository.set_status(event)
