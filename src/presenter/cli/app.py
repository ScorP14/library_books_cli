from domain.services import ServicesBook
from infrastructure.repository.books.json_repo import BookRepositoryJson
from presenter.cli.view import (
    add_book,
    delete_book,
    search_book,
    get_all_books,
    set_status,
)
from settings.config import PATH_JSON_DB


def get_command_number():
    print()
    print("Команды: ")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Поиск книги")
    print("4. Отобразить все книги")
    print("5. Изменить статус книги")
    print("6. Выход")
    choice = int(input("Выберите команду: "))
    return choice


def start_app():
    repository_book = BookRepositoryJson(PATH_JSON_DB)
    service_book = ServicesBook(repository_book)
    while True:
        try:
            command: int = int(get_command_number())
        except ValueError:
            print("Ошибка ввода, попробуйте снова.")
            continue
        match command:
            case 1:  # Добавить книгу.
                add_book(service_book)
            case 2:  # Удалить книгу
                delete_book(service_book)
            case 3:  # Поиск книги
                search_book(service_book)
            case 4:  # Отобразить все книги
                get_all_books(service_book)
            case 5:  # Изменить статус книги
                set_status(service_book)
            case 6:  # Выход
                break
            case _:
                print("Ошибка ввода, попробуйте снова.")


if __name__ == "__main__":
    start_app()
