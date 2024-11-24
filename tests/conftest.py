import pytest
from domain.book.entity import StatusEnum, Book
from domain.book.services import ServicesBook
from tests.domain.book.mock_repo_book import BookRepositoryTest

list_data_book = [
    dict(
        id=1,
        title="Название 1",
        author="Автор 1",
        year=2001,
        status=StatusEnum.STOCK.value,
    ),
    dict(
        id=2,
        title="Название 2",
        author="Автор 2",
        year=2002,
        status=StatusEnum.ISSUED.value,
    ),
    dict(
        id=3,
        title="Название 3",
        author="Автор 3",
        year=2003,
        status=StatusEnum.STOCK.value,
    ),
    dict(
        id=4,
        title="Название 4",
        author="Автор 4",
        year=2004,
        status=StatusEnum.ISSUED.value,
    ),
]


@pytest.fixture(params=list_data_book)
def data_book(request):
    return request.param


@pytest.fixture(params=[Book(**item) for item in list_data_book])
def instance_book(request):
    return request.param


@pytest.fixture(scope="session")
def repository():
    return BookRepositoryTest()


@pytest.fixture(scope="session")
def service(repository):
    return ServicesBook(repository)
