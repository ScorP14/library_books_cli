from dataclasses import dataclass, asdict

from domain.entity import StatusEnum


@dataclass
class CreateBook:
    title: str
    author: str
    year: int
    status: str = StatusEnum.STOCK.value

    def as_dict(self):
        return asdict(self)


@dataclass
class DeleteBook:
    id: int


@dataclass
class SetStatusBook:
    id: int
    status: StatusEnum
