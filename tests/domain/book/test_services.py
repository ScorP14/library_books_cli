import pytest

from domain.book.entity import Book, StatusEnum
from exeption.repository import NotFoundByIdError

data_for_add = [
    dict(title='Название 1', author='Автор 1', year=2001),
    dict(title='Название 2', author='Автор 2', year=2002),
    dict(title='Название 3', author='Автор 3', year=2003),
]

instance_books = [
    Book(**item | {'id': index, 'status': StatusEnum.STOCK})
    for index, item in enumerate(data_for_add)
]


def test_first_get_all_book(service):
    assert service.get_all_book() == []


@pytest.mark.parametrize(
    'title, author, year, _id',
    [
        ('Название 1', 'Автор 1', 2001, 0),
        ('Название 2', 'Автор 2', 2002, 1),
        ('Название 3', 'Автор 3', 2003, 2),
    ]

)
def test_add_book(service, title, author, year, _id):
    book = service.add_book(title, author, year)
    assert book.id == _id
    assert book.title == title
    assert book.author == author
    assert book.year == year


def test_all_book(service):
    books = service.get_all_book()
    assert books == instance_books


@pytest.mark.parametrize('_id', [0, 1, 2])
def test_delete_book(service, _id):
    service.delete_book(_id)


@pytest.mark.parametrize('_id', [0, 1, 2])
def test_delete_book_error(service, _id):
    with pytest.raises(NotFoundByIdError):
        service.delete_book(_id)


