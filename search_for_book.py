def book_list_view(library):
    """Выводит названия всех книг в библиотеке.
    Если книг нет — выводит сообщение об этом."""
    if not library:
        print("В библиотеке нет книг.")
        return

    print("\nСписок книг в библиотеке:")
    for i, book_name in enumerate(library.keys(), 1):
        print(f"{i}. {book_name}")


def add_book(library, book_name, author, year):
    """Добавляет новую книгу в библиотеку.
    Если книга уже существует — предлагает обновить информацию."""
    action = "добавлена"

    if book_name in library:
        action = "обновлена"
        print(f"Книга '{book_name}' уже существует.")
        choice = input("Обновить информацию? (да/нет): ").strip().lower()
        if choice != 'да':
            print("Операция отменена.")
            return

    library[book_name] = {
        'author': author,
        'year_of_publication': year,
        'availability': True
    }
    print(f"Книга '{book_name}' успешно {action}.")


def remove_book(library, book_name):
    """Удаляет книгу из библиотеки.
        Если книга не найдена выводит сообщение об этом."""
    if book_name in library:
        del library[book_name]
        print(f"Книга ' {book_name}' успешно удалена из библиотеки.")
    else:
        print(f"Книга '{book_name}' не найдена в библиотеке.")


def issue_book(library, book_name):
    """Отмечает книгу как выданную."""
    if book_name not in library:
        print(f"Книга '{book_name}' не найдена в библиотеке.")
        return

    if library[book_name]['availability'] is False:
        print(f"Книга '{book_name}' уже выдана.")
        return

    library[book_name]['availability'] = False
    print(f"Книга '{book_name}' успешно выдана.")


def return_book(library, book_name):
    """Отмечает книгу как возвращённую."""
    if book_name not in library:
        print(f"Книга '{book_name}' не найдена в библиотеке.")
        return

    if library[book_name]['availability'] is True:
        print(f"Книга '{book_name}' уже находится в библиотеке.")
        return

    library[book_name]['availability'] = True
    print(f"Книга '{book_name}' успешно возвращена в библиотеку.")


def find_book(library, title):
    """Поиск книги по части названия."""
    if not title.strip():
        print("Поисковый запрос не может быть пустым.")
        return

    found = False
    for book_name in library.keys():
        if title.lower() in book_name.lower():
            book = library[book_name]
            status = ("В библиотеке" if book['availability'] else "Выдана")

            print(f"\nНазвание:      {book_name}")
            print(f"Автор:           {book['author']}")
            print(f"Год издания:     {book['year_of_publication']}")
            print(f"Статус:          {status}")
            print("-" * 40)
            found = True

    if not found:
        print(f"Книги, содержащие '{title}' не найдены.")


def show_menu():
    print("\n" + "="*55)
    print("               БИБЛИОТЕКА КНИГ")
    print("="*55)
    print("1. Добавить книгу")
    print("2. Показать список всех книг")
    print("3. Найти книгу")
    print("4. Выдать книгу")
    print("5. Вернуть книгу")
    print("6. Удалить книгу")
    print("0. Выход из программы")
    print("="*55)


library = {}

while True:
    show_menu()
    choice = input("Выберите действие (0-6): ").strip()

    if choice == '1':
        book_name = input("Введите название книги: ").strip()
        if not book_name:
            print("Название не может быть пустым.")
            continue
        author = input("Введите автора: ").strip()
        if not author:
            print("Автор не может быть пустым.")
            continue
        try:
            year = int(input("Введите год издания: ").strip())
        except ValueError:
            print("Год издания должен быть числом.")
            continue
        add_book(library, book_name, author, year)

    elif choice == '2':
        book_list_view(library)

    elif choice == '3':
        title = input("Введите название книги (или её часть): ").strip()
        find_book(library, title)

    elif choice == '4':
        title = input("Введите название книги для выдачи: ").strip()
        issue_book(library, title)

    elif choice == '5':
        title = input("Введите название книги для возврата: ").strip()
        return_book(library, title)

    elif choice == '6':
        title = input("Введите название книги для удаления: ").strip()
        remove_book(library, title)

    elif choice == '0':
        print("\nПрограмма завершена. До свидания!")
        break

    else:
        print("Неверный выбор. Введите число от 0 до 6.")