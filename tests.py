import os
import random

from book import Book, BookStatus
from file_manager import JsonBookFileManager
from library import Library


class TestBook:
    def __init__(self) -> None:
        self.books_count = 0

        test_file_manager = JsonBookFileManager(file_path="test.json")
        self.library = Library(file_manager=test_file_manager)
        self.file_manager = test_file_manager

    def __enter__(self) -> "TestBook":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        file_path = self.file_manager.file_path
        if os.path.exists(file_path):
            os.remove(file_path)

    def run(self) -> None:
        self._test_add_books()
        self._test_search_books()
        self._test_all_books()
        self._test_remove_book()
        self._test_change_book_status()

    def _test_add_books(self) -> None:
        assert self.library.count == self.books_count
        for i in range(1, 21):
            self.library.add_book(
                title=f"Title {i}",
                author="Author",
                year=random.randint(1000, 2024),
            )
            self.books_count += 1
            assert self.library.count == self.books_count
        self.library.add_book(title="Title 2", author="Author 2", year=2000)
        self.books_count += 1
        assert self.library.count == self.books_count

        print("Add book checked")

        self._test_status_after_create()

    def _test_status_after_create(self) -> None:
        assert all(
            [
                book["status"] == BookStatus.available.value
                for book in self.library.get_books()
            ]
        )

        print("Status after created checked")

    def _test_search_books(self) -> None:
        book = self.library.search_book("Author")

        assert book["title"] == "Title 1"
        assert book["author"] == "Author"
        for field in Book.__dataclass_fields__.keys():
            assert field in book

        book = self.library.search_book("Title")
        assert book == []

        book = self.library.search_book("Title 6")
        assert book["title"] == "Title 6"
        assert book["author"] == "Author"

        book = self.library.search_book("2000")
        assert book["title"] == "Title 2"
        assert book["author"] == "Author 2"
        assert book["year"] == 2000

        print("Search book checked")

    def _test_all_books(self) -> None:
        books = self.library.get_books()
        assert len(books) == self.library.count

        print("Get all books checked")

    def _test_remove_book(self) -> None:
        self.library.remove_book(book_id=2)
        self.library.remove_book(book_id=6)
        self.library.remove_book(book_id=17)
        self.books_count -= 3
        assert self.library.count == self.books_count

        print("Remove book checked")

    def _test_change_book_status(self) -> None:
        book = self.library.change_status(1, BookStatus.unavailable)
        assert isinstance(book, dict)
        assert book["status"] == BookStatus.unavailable.value

        book = self.library.change_status(5, BookStatus.available)
        assert isinstance(book, dict)
        assert book["status"] == BookStatus.available.value

        print("Status checked")


def run_test() -> None:
    with TestBook() as tests:
        tests.run()


if __name__ == "__main__":
    run_test()
