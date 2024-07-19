import json
import os
from abc import ABC, abstractmethod


class BookFileManager(ABC):
    """
    Абстрактный класс отвечающий за сохранение и загрузку данных о книгах.

    Переопределение методов:
        def loads() -> возвращает словарь книг

        def save(data: dict)- ожидает получить словарь данных о книгах
    """

    @abstractmethod
    def loads(self) -> dict:
        ...

    @abstractmethod
    def save(self, data: dict) -> None:
        ...


class JsonBookFileManager(BookFileManager):
    def __init__(self, file_path: str = "books.json") -> None:
        """
        :param file_path: путь файла
        """
        super().__init__()
        self.file_path = os.path.join(os.path.dirname(__file__), file_path)

    def loads(self) -> dict[int, dict]:
        """
        :return: словарь с ключом id книги и значениями книги включая id
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return {int(book_id): v for book_id, v in data.items()}
        return {}

    def save(self, data: dict[int, dict]) -> None:
        """
        :param data: словарь с ключом id книги и значениями книги
        """
        with open(self.file_path, "w") as f:
            json.dump(data, f)
