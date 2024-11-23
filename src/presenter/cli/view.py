from domain.services import ServicesBook
from exeption.repository import NotFoundByIdError
from presenter.cli.helper import print_sequence_books


def add_book(service_book: ServicesBook):
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    try:
        year = int(input("Введите год издания книги: "))
    except ValueError:
        print("Некорректный год")
        print("Книга не добавлена.")
        return
    service_book.add_book(title=title, author=author, year=year)
    print("Книга успешно добавлена.")


def delete_book(service_book: ServicesBook):
    try:
        book_id = int(input("Введите ID книги для удаления: "))
    except ValueError:
        print("Некорректно введен ID, попробуйте снова.")
        return
    try:
        service_book.delete_book(book_id)
        print("Книга удалена.")
    except NotFoundByIdError as e:
        print(e.message())


def search_book(service_book: ServicesBook):
    query = input("Введите название, автора или год для поиска: ")
    books = service_book.search_book(query)
    (
        print_sequence_books(books)
        if books
        else print(f'Книги по запросу <"{query}"> не найдены. ')
    )


def get_all_books(service_book: ServicesBook):
    books = service_book.get_all_book()
    (
        print_sequence_books(books)
        if books
        else print('Нет записей. Воспользуйтесь "1. Добавить книгу. "')
    )


def set_status(service_book: ServicesBook):
    try:
        book_id = int(input("Введите ID книги для изменения статуса: "))
    except ValueError:
        print("Некорректный ID.")
        print("Статус не изменен. Попробуйте снова.")
        return
    print()
    print("1. В наличии.")
    print("2. Выдана.")
    try:
        number_status = int(input("Введите новый статус: "))
    except ValueError:
        print("Некорректный номер статуса. ")
        print("Статус не изменен. Попробуйте снова.")
        return
    match number_status:
        case 1:
            new_status = "в наличии"
        case 2:
            new_status = "выдана"
        case _:
            print("Ошибка ввода, попробуйте снова. ")
            return
    try:
        service_book.set_status_book(book_id, new_status)
        print("Статус книги изменен. ")
    except NotFoundByIdError as e:
        print(e.message())
