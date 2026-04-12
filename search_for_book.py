def book_list_view(library):
    """Выводит названия всех книг в библиотеке."""
    if not library:
        print("В библиотеке нет книг.")
        return

    print("\nСписок книг в библиотеке:")
    for i, book_name in enumerate(library.keys(), 1):
        print(f"{i}. {book_name}")


def add_book(library, book_name=None, author=None, year=None):
    """Добавляет или обновляет книгу в библиотеке."""
    if book_name is None:
        book_name = input("Введите название книги: ").strip()
    if not book_name:
        print("Название книги не может быть пустым.")
        return
    author = input("Введите автора: ").strip()
    year = int(input("Введите год издания: ").strip())

    if book_name in library:
        print(f"Книга '{book_name}' уже существует.")
        choice = input("Обновить информацию? (да\нет): ").strip().lower()
        if choice != 'да':
            print("Операция отменена.")
            return

    library[book_name] = {
        'author': author,
        'year_of_publication': year,
        'availability': None
    }

    action = "обновлена" if book_name in library else "добавлена"
    print(f"Книга '{book_name}' успешно {action} в библиотеке.")


def remove_book(library, book_name=None):
    """Удаляет книгу из библиотеки."""
    if book_name is None:
        book_name = input("\nВведите название книги для удаления: ").strip()

    if book_name in library:
        del library[book_name]
        print(f"Книга ' {book_name}' успешно удалена из библиотеки.")
    else:
        print(f"Книга '{book_name}' не найдена в библиотеке.")


def issue_book(library, book_name=None):
    """Отмечает книгу как выданную (availability = False)"""
    if book_name is None:
        book_name = input("\nВведите название книги для выдачи: ").strip()

    if book_name not in library:
        print(f"Книга '{book_name}' не найдена в библиотеке.")
        return

    if library[book_name]['availability'] is False:
        print(f"Книга '{book_name}' уже выдана.")
        return

    library[book_name]['availability'] = False
    print(f"Книга '{book_name}' успешно выдана.")


def return_book(library, book_name=None):
    """Отмечает книгу как возвращённую (availability = True)"""
    if book_name is None:
        book_name = input("\nВведите название книги для возврата: ").strip()

    if book_name not in library:
        print(f"Книга '{book_name}' не найдена в библиотеке.")
        return

    if library[book_name]['availability'] is True:
        print(f"Книга '{book_name}' уже находится в библиотеке.")
        return

    library[book_name]['availability'] = True
    print(f"Книга '{book_name}' успешно возвращена в библиотеку.")


def find_book(library):
    """Поиск книги по названию."""
    search_query = input("\nВведите название книги (или ее часть): ").strip()
    if not search_query:
        print("Поиск при запросе не может быть пустым")
        return
    found = False

    for book_name in library.keys():
        if search_query.lower() in book_name.lower():
            book = library[book_name]

            if book['availability'] is None:
                status = "В библиотеке (статус не определен)"
            elif book['availability'] is False:
                status = "Выдана"
            else:
                status = "В наличии"

            print(f"Название: '{book_name}':")
            print(f"Автор: {book['author']}")
            print(f"Год издания: {book['year_of_publication']}")
            print(f"Статус: {status}")
            print("-" * 40)
            found = True

    if not found:
        print(f"Книги, содержащие '{search_query}' не найдены.")

def show_menu():
    """Показывает главное меню"""
    print("\n" + "="*50)
    print("               БИБЛИОТЕКА КНИГ")
    print("="*50)
    print("1. Добавить книгу")
    print("2. Показать список всех книг")
    print("3. Найти книгу")
    print("4. Выдать книгу")
    print("5. Вернуть книгу")
    print("6. Удалить книгу")
    print("0. Выход из программы")
    print("="*50)


library = {}

menu_actions = {
    '1': lambda: add_book(library),
    '2': lambda: book_list_view(library),
    '3': lambda: find_book(library),
    '4': lambda: issue_book(library),
    '5': lambda: return_book(library),
    '6': lambda: remove_book(library),
    '0': lambda: print("\nПрограмма завершена. До свидания!") or exit(0)
}

while True:
    show_menu()
    choice = input("Выберите действие (0-6): ").strip()

    if choice in menu_actions:
        menu_actions[choice]()
    else:
        print("Неверный выбор. Пожалуйста, введите число от 0 до 6.")