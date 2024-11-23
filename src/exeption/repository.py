from dataclasses import dataclass
from typing import Any


@dataclass
class IRepositoryError(Exception):
    value: Any = None

    def message(self):
        return NotImplementedError()


class NotFoundByIdError(IRepositoryError):
    value = int

    def message(self):
        return f"Книги с ID({self.value}) не найдена. "
