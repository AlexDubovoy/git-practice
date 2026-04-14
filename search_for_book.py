def book_list_view(library):
    """Выводит названия всех книг в библиотеке."""
    if not library:
        print("В библиотеке нет книг.")
        return
    print("\nСписок книг в библиотеке:")
    for i, book_name in enumerate(library.keys(), 1):
        print(f"{i}. {book_name}")


def add_book(library, book_name=None, author=None, year=None):
    """Добавляет или обновляет книгу."""
    if book_name is None:
        book_name = input("Введите название книги: ").strip()
    if not book_name:
        print("Название книги не может быть пустым.")
        return
    author = input("Введите автора: ").strip()
    try:
        year = int(input("Введите год издания: ").strip())
    except ValueError:
        print("Год издания должен быть числом.")
        return

    if book_name in library:
        print(f"Книга '{book_name}' уже существует.")
        choice = input("Обновить информацию? (да/нет): ").strip().lower()
        if choice != 'да':
            print("Операция отменена.")
            return

    library[book_name] = {
        'author': author,
        'year_of_publication': year,
        'availability': None
    }
    print(f"Книга '{book_name}' успешно добавлена.")


def remove_book(library, book_name=None):
    if book_name is None:
        book_name = input("\nВведите название книги для удаления: ").strip()
    if book_name in library:
        del library[book_name]
        print(f"Книга '{book_name}' успешно удалена.")
    else:
        print(f"Книга '{book_name}' не найдена.")


def issue_book(library, book_name=None):
    if book_name is None:
        book_name = input("\nВведите название книги для выдачи: ").strip()
    if book_name not in library:
        print(f"Книга '{book_name}' не найдена.")
        return
    if library[book_name]['availability'] is False:
        print(f"Книга '{book_name}' уже выдана.")
        return
    library[book_name]['availability'] = False
    print(f"Книга '{book_name}' успешно выдана.")


def return_book(library, book_name=None):
    if book_name is None:
        book_name = input("\nВведите название книги для возврата: ").strip()
    if book_name not in library:
        print(f"Книга '{book_name}' не найдена.")
        return
    if library[book_name]['availability'] is True:
        print(f"Книга '{book_name}' уже в библиотеке.")
        return
    library[book_name]['availability'] = True
    print(f"Книга '{book_name}' успешно возвращена.")


def find_book(library, title=None):
    """Поиск книги по части названия."""
    if title is None:
        title = input("\nВведите название книги (или ее часть): ").strip()

    if not title:
        print("Поисковый запрос не может быть пустым.")
        return

    found = False
    for book_name in library.keys():
        if title.lower() in book_name.lower():
            book = library[book_name]
            status = ("В библиотеке (статус не определён)" if book['availability'] is None else
                      "Выдана" if book['availability'] is False else
                      "В наличии")

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

menu = {
    '1': ("Добавить книгу", lambda: add_book(library)),
    '2': ("Показать список всех книг", lambda: book_list_view(library)),
    '3': ("Найти книгу", lambda: find_book(library)),
    '4': ("Выдать книгу", lambda: issue_book(library)),
    '5': ("Вернуть книгу", lambda: return_book(library)),
    '6': ("Удалить книгу", lambda: remove_book(library)),
    '0': ("Выход из программы", lambda: print("\nПрограмма завершена. До свидания! Всего ХоРоШеГо!!!") or exit(0))
}


while True:
    show_menu()
    choice = input("Выберите действие (0-6): ").strip()

    if choice in menu:
        menu[choice][1]()
    else:
        print("Неверный выбор. Пожалуйста, введите число от 0 до 6.")