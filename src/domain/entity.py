from dataclasses import dataclass
from enum import Enum
from typing import Any


class StatusEnum(Enum):
    STOCK = "в наличии"
    ISSUED = "выдана"


@dataclass(frozen=True)
class IEntity:
    pass


@dataclass(frozen=True)
class Book(IEntity):
    id: int
    title: str
    author: str
    year: int
    status: StatusEnum


class MapperBook:
    @staticmethod
    def from_dict_to_model(data: dict[str, Any]) -> Book:
        return Book(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=StatusEnum(data["status"]),
        )

    @staticmethod
    def from_model_to_dict(book: Book) -> dict[str, Any]:
        return dict(
            id=book.id,
            title=book.title,
            author=book.author,
            year=book.year,
            status=book.status.value,
        )
