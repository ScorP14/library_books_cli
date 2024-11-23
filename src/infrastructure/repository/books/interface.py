from typing import Protocol, Sequence

from domain.entity import Book
from domain.event import CreateBook, DeleteBook, SetStatusBook


class IBookRepository(Protocol):
    def add(self, event: CreateBook) -> Book:
        """Добавить книгу в репозиторий. Вернуть экземпляр книги."""

    def delete(self, event: DeleteBook) -> None:
        """Удалить книгу из репозитория."""

    def search(self, query: str) -> Sequence[Book] | None:
        """Поиск книги в репозитории. Вернуть массив книг или ничего."""

    def all(self) -> Sequence[Book]:
        """Получить все книги из репозитория."""

    def set_status(self, event: SetStatusBook) -> None:
        """Изменить статус книги."""
