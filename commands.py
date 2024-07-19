from datetime import datetime
from typing import Callable

from library import Library
from utils import get_int_input, get_str_input, get_book_status_input

MAX_BOOKS = 20

current_library = Library()


def add_book() -> None:
    """Обработчик команды добавления книги."""
    title = get_str_input("Введите название книги: ")
    author = get_str_input("Введите автора книги: ")
    current_year = datetime.now().year
    while True:
        year = get_int_input(
            "Введите год издания книги: ",
            "Год издания должен быть числом.",
        )
        if year <= current_year:
            break
        print(f"Год издания не должен превышать текущий год ({current_year}).")

    current_library.add_book(title, author, int(year))


def delete_book() -> None:
    """Обработчик команды удаления книги."""
    book_id = get_int_input(
        "Введите id книги, которую хотите удалить: ",
        "id книги должен быть числом.",
    )
    current_library.remove_book(book_id)


def search_book() -> None:
    """Обработчик команды поиска книги."""
    book = current_library.search_books(
        get_str_input("Введите название книги, автора или год издания книги: ")
    )
    if book:
        print(book)
    else:
        print("Не удалось найти подходящую книгу.")


def get_books() -> None:
    """Обработчик команды получения всех книг."""
    books = current_library.get_books()
    if not books:
        print("Здесь еще нету книг.")
        return

    for i, book in enumerate(books):
        if i % MAX_BOOKS == 0 and i != 0:
            question = input("Продолжить? (Enter)")
            if question:
                return
        print(book)


def change_status() -> None:
    """Обработчик команды изменения статуса книги."""
    book_id = get_int_input(
        "Введите id книги, в которой хотите изменить статус: ",
        "id книги должен быть числом.",
    )
    if not current_library.has_book(book_id):
        return
    status = get_book_status_input()
    current_library.change_status(book_id, status)


MAIN_COMMANDS: list[str] = [
    "1. Добавление книги",
    "2. Удаление книги",
    "3. Поиск книги",
    "4. Отображение всех книг",
    "5. Изменение статуса книги",
]
main_command_funcs: dict[int, Callable] = {
    1: add_book,
    2: delete_book,
    3: search_book,
    4: get_books,
    5: change_status,
}
