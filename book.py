from dataclasses import dataclass
from enum import Enum


class BookStatus(Enum):
    """Статусы книг."""

    available = "В наличии"
    unavailable = "Выдана"


STATUS_ITEMS = {
    1: BookStatus.available,
    2: BookStatus.unavailable,
}


@dataclass
class Book:
    """Дата класс представления книги."""

    id: int
    title: str
    author: str
    year: int
    status: BookStatus
