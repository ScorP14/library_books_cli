from dataclasses import dataclass
from typing import Sequence, Any
import json
import os

from domain.entity import Book, MapperBook
from domain.event import CreateBook, DeleteBook, SetStatusBook
from exeption.repository import NotFoundByIdError
from infrastructure.repository.books.interface import IBookRepository


@dataclass
class JsonDTO:
    metadata: dict[str, Any]
    data: dict[str, dict]

    def get_all(self) -> dict[str, dict]:
        return dict(metadata=self.metadata, data=self.data)


@dataclass
class BookRepositoryJson(IBookRepository):
    path_to_file: str

    def __post_init__(self):
        """Инициализируем JSON-файл, если его нет. """
        if not os.path.exists(self.path_to_file):

            result = JsonDTO(metadata=dict(autoincrement=0), data={})
            self._save_books(result)

    def add(self, event: CreateBook) -> Book:
        """Добавить книгу в репозиторий"""
        database: JsonDTO = self._load_books()

        _id = database.metadata["autoincrement"]
        database.data[_id] = event.as_dict()
        database.metadata["autoincrement"] += 1

        self._save_books(database)
        book = MapperBook.from_dict_to_model({"id": _id} | event.as_dict())
        return book

    def delete(self, event: DeleteBook) -> None:
        """Удалить книгу из репозитория."""
        database: JsonDTO = self._load_books()

        str_id = str(event.id)
        if str_id not in database.data:
            raise NotFoundByIdError(event.id)
        del database.data[str_id]

        self._save_books(database)

    def search(self, query: str) -> Sequence[Book] | None:
        """Поиск книги в репозитории. Вернуть массив книг или ничего."""
        database: JsonDTO = self._load_books()

        result = []
        for _id, book in database.data.items():
            if (
                book["title"] == query
                or book["author"] == query
                or (query.isdigit() and book["year"] == int(query))
            ):
                result.append(MapperBook.from_dict_to_model({"id": _id} | book))
        return result

    def all(self) -> Sequence[Book]:
        """Получить все книги из репозитория."""
        database: JsonDTO = self._load_books()

        return [
            MapperBook.from_dict_to_model({"id": _id} | book)
            for _id, book in database.data.items()
        ]

    def set_status(self, event: SetStatusBook) -> None:
        """Изменить статус книги."""
        database: JsonDTO = self._load_books()

        str_id = str(event.id)
        if str_id not in database.data:
            raise NotFoundByIdError(event.id)

        database.data[str_id]["status"] = event.status.value

        self._save_books(database)

    def _save_books(self, data: JsonDTO):
        with open(self.path_to_file, "w", encoding="utf-8") as file:
            json.dump(data.get_all(), file, ensure_ascii=False, indent=4)

    def _load_books(self) -> JsonDTO:
        with open(self.path_to_file, "r", encoding="utf-8") as file:
            result_data = json.load(file)
            return JsonDTO(metadata=result_data["metadata"], data=result_data["data"])
