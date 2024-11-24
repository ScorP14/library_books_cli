from dataclasses import dataclass, field
from typing import Sequence

from domain.book.entity import Book, MapperBook
from domain.book.event import CreateBook, DeleteBook, SetStatusBook
from exeption.repository import NotFoundByIdError
from infrastructure.repository.books.interface import IBookRepository


@dataclass
class BookRepositoryTest(IBookRepository):
    storage: dict = field(default_factory=dict)
    autoincrement: int = field(default=0)

    def add(self, event: CreateBook) -> Book:
        self.storage[self.autoincrement] = event.as_dict()
        book = MapperBook.from_dict_to_model(
            {"id": self.autoincrement} | event.as_dict()
        )
        self.autoincrement += 1
        return book

    def delete(self, event: DeleteBook) -> None:
        if event.id not in self.storage:
            raise NotFoundByIdError(event.id)
        del self.storage[event.id]

    def search(self, query: str) -> Sequence[Book] | None:
        result = []
        for _id, book in self.storage.items():
            if (
                book["title"] == query
                or book["author"] == query
                or (query.isdigit() and book["year"] == int(query))
            ):
                result.append(MapperBook.from_dict_to_model({"id": _id} | book))
        return result

    def all(self) -> Sequence[Book]:
        return [
            MapperBook.from_dict_to_model({"id": _id} | book)
            for _id, book in self.storage.items()
        ]

    def set_status(self, event: SetStatusBook) -> None:
        str_id = str(event.id)
        if str_id not in self.storage:
            raise NotFoundByIdError(event.id)
        self.storage[str_id]["status"] = event.status.value
