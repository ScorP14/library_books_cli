from domain.book.entity import Book, MapperBook


def test_book_creation_instance(data_book: dict):
    book_instance = Book(
        id=data_book["id"],
        title=data_book["title"],
        author=data_book["author"],
        year=data_book["year"],
        status=data_book["status"],
    )
    assert book_instance.id == data_book["id"]
    assert book_instance.title == data_book["title"]
    assert book_instance.author == data_book["author"]
    assert book_instance.year == data_book["year"]
    assert book_instance.status == data_book["status"]


def test_book_mapping(data_book: dict):
    from_dict_to_model = MapperBook.from_dict_to_model(
        dict(
            id=data_book["id"],
            title=data_book["title"],
            author=data_book["author"],
            year=data_book["year"],
            status=data_book["status"],
        )
    )
    from_model_to_dict = MapperBook.from_model_to_dict(from_dict_to_model)
    assert from_model_to_dict == data_book
