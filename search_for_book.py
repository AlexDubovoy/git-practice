def book_list_view(library):
    """Выводит названия всех книг в библиотеке."""
    if not library:
        print("В библиотеке нет книг.")
        return

    print("\nСписок книг в библиотеке:")
    for i, book_name in enumerate(library.keys(), 1):
        print(f"{i}. {book_name}")


def add_book(library):
    """Добавляет новую книгу в библиотеку."""
    print("\n- - - Добавление новой книги - - -")
    book_name = input("Введите название книги: ").strip()

    if not book_name:
        print("Ошибка: Название книги не может быть пустым.")
        return

    is_update = False
    if book_name in library:
        print(f"Книга '{book_name}' уже существует в библиотеке.")
        choice = input("Хотите обновить информацию о книге? (да/нет): ").strip().lower()
        if choice != 'да':
            print("Операция отменена.")
            return
        is_update = True

    author = input("Введите автора книги: ").strip()
    year =int(input("Введите год издания: ").strip())

    library[book_name] = {
        'author': author,
        'year_of_publication': year,
        'availability': None
    }

    action = "обновлена" if is_update else "добавлена"
    print(f"Книга '{book_name}' успешно {action} в библиотеке.")


def remove_book(library):
    """Удаляет книгу из библиотеки."""
    book_name = input("\nВведите название книги для удаления: ").strip()
    if book_name in library:
        del library[book_name]
        print(f"Книга ' {book_name}' успешно удалена из библиотеки.")
    else:
        print(f"Книга '{book_name}' не найдена в библиотеке.")


def issue_book(library):
    """Отмечает книгу как выданную (availability = False)"""
    book_name = input("\nВведите название книги для выдачи: ").strip()
    if book_name not in library:
        print(f"Книга '{book_name}' не найдена в библиотеке.")
        return

    if library[book_name]['availability'] is False:
        print(f"Книга '{book_name}' уже выдана.")
        return

    library[book_name]['availability'] = False
    print(f"Книга '{book_name}' успешно выдана.")


def return_book(library):
    """Отмечает книгу как возвращённую (availability = True)"""
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

    found_books = []

    for book_name in library.keys():
        if search_query.lower() in book_name.lower():
            found_books.append(book_name)

    if not found_books:
        print(f"Книги, содержащие '{search_query}' в название не найдены.")
        return

    print(f"\nНайдено книг: {len(found_books)}\n")

    for book_name in found_books:
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

while True:
    show_menu()
    choice = input("Выберите действие (0-6): ").strip()

    if choice == '1':
        add_book(library)
    elif choice == '2':
        book_list_view(library)
    elif choice == '3':
        find_book(library)
    elif choice == '4':
        issue_book(library)
    elif choice == '5':
        return_book(library)
    elif choice == '6':
        remove_book(library)
    elif choice == '0':
        print("\nПрограмма завершена. До встречи!")
        break
    else:
        print("Неверный выбор. Пожалуйста, введите число от 0 до 6.")