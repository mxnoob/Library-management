from dataclasses import asdict
from typing import Union

from book import Book, BookStatus
from file_manager import BookFileManager, JsonBookFileManager

BOOKS_JSON = "books.json"


class Library:
    """Класс библиотеки"""

    def __init__(self, file_manager: BookFileManager = None):
        """
        :param file_manager: менеджер по работе с файлом данных о книгах.
        """
        self.books: dict[int, dict] = dict()
        if file_manager is None:
            file_manager = JsonBookFileManager()
        self.file_manager = file_manager
        self._load_books()
        self._last_book_id: int = max(self.books) if self.books else 0

    def get_next_book_id(self) -> int:
        self._last_book_id += 1
        return self._last_book_id

    def has_book(self, book_id: int) -> bool:
        """Проверяет существование книги."""
        if book_id in self.books:
            return True
        print(f"Книги с `id={book_id}` не существует")

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавление новой книги."""
        next_book_id = self.get_next_book_id()
        book = Book(
            next_book_id, title, author, year, BookStatus.available.value
        )
        self.books[next_book_id] = asdict(book)
        self._save_books()

    def remove_book(self, book_id: int) -> None:
        """Удаление книги по id."""
        if self.has_book(book_id):
            del self.books[book_id]
            self._save_books()

    def search_books(
        self, search: str, is_one_book: bool = True
    ) -> Union[list[dict], dict]:
        """Поиск книг по названию, автору или году издания.
        :param search: текст поиска
        :param is_one_book: искать одну книги или весь список
        """
        books = []
        for book in self.books.values():
            if search in (book["title"], book["author"], str(book["year"])):
                if is_one_book:
                    return book
                books.append(book)
        return books

    def get_books(self) -> list[dict]:
        """Возвращает список всех книг."""
        return list(self.books.values())

    def change_status(self, book_id: int, status: BookStatus) -> None:
        """Изменить статус книги."""
        if self.has_book(book_id):
            self.books[book_id]["status"] = status.value
            self._save_books()

    def _load_books(self):
        """Загрузить книги из файла."""
        self.books = self.file_manager.loads()

    def _save_books(self):
        """Сохранить данные о книгах в файл."""
        self.file_manager.save(self.books)
