# Library management

### Консольное приложение для управления библиотекой книг. Не используя сторонние библиотеки

### Функционал приложения:
1. Добавление книги (`название`, `автор`, `год издания`)
2. Удаление книги по `id`
3. Поиск книги осуществляется точным вхождением по `названию`, `автору` или `году издания`
4. Отображение всех книг (выдаёт книги порциями по `20`, можно изменить в настройках команд)
5. Изменение статуса книги по `id`, `status` (`В наличии`, `Выдана`)

### Запуск приложения

```shell
python main.py
```

### Запуск тестов

```shell
python tests.py
```