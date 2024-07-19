from book import BookStatus, STATUS_ITEMS
from exceptions import BreakerException

STOP_WORDS = ("отмена", "прервать", "стоп", "break", "stop")


def breakable_input(message: str = "") -> str:
    """ВВод с возможностью прервать команду."""
    text = input(message).strip()
    if text.lower() in STOP_WORDS:
        raise BreakerException
    return text


def get_int_input(message: str, error_message: str) -> int:
    """Ввод числового значения."""
    while True:
        number = breakable_input(message)
        if number.isdigit():
            return int(number)
        else:
            print(error_message)


def get_str_input(message: str) -> str:
    """Ввод строчного значения"""
    while True:
        string = breakable_input(message)
        if string:
            return string
        print("Нельзя ввести пустое значение")


def get_book_status_input() -> BookStatus:
    """Выбор статуса для книги."""
    print("\n".join(f"{i}. {v.value}" for i, v in STATUS_ITEMS.items()))
    print("Выберите один из статусов: ", end="")
    while True:
        number = breakable_input()
        if number.isdigit() and int(number) in STATUS_ITEMS:
            return STATUS_ITEMS[int(number)]
        else:
            print(f"Выберите один из предложенных вариантов: ", end="")
