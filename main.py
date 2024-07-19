from commands import main_command_funcs, MAIN_COMMANDS
from exceptions import BreakerException
from utils import STOP_WORDS


def main() -> None:
    """Функция старта приложения."""

    while True:
        print("\n".join(MAIN_COMMANDS))
        command: str = input("Выберите команду которую хотите выполнить: ")
        if command.isdigit() and 0 <= int(command) - 1 < len(MAIN_COMMANDS):
            book_command = main_command_funcs[int(command)]
            print(
                f"Можно прервать операцию, путем ввода одного из слов: {', '.join(STOP_WORDS)!r}"
            )
            try:
                book_command()
            except BreakerException:
                print("Операция была прервана...")
        else:
            print(f"Выберите команду из списка от 1 до {len(MAIN_COMMANDS)}.")
        print()


if __name__ == "__main__":
    main()
