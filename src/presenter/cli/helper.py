from typing import Sequence

from domain.entity import Book


def print_sequence_books(books: Sequence[Book]) -> None:
    for book in books:
        print(
            f"<ID-{book.id}> {book.title} {book.year}г. ({book.author}). '{book.status.value}'"
        )
