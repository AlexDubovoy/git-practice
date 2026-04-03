def book_list_view(library):
    """Выводит названия всех книг в библиотеке.
    Если книг нет — выводит сообщение об этом."""
    if not library:
        print("В библиотеке нет книг.")
        return

    print("Список книг в библиотеке:")
    for i, book_name in enumerate(library.keys(), 1):
        print(f"{i}. {book_name}")


def add_book(library, book_name, author, year):
    """Добавляет новую книгу в библиотеку.
    Если книга уже существует — предлагает обновить информацию."""
    if book_name in library:
        print(f"Книга '{book_name}' уже существует в библиотеке.")
        choice = input("Хотите обновить информацию о книге? (да/нет): ").strip().lower()

        if choice != 'да':
            print("Обновление отменено.")
            return

    # Добавляем или обновляем книгу
    library[book_name] = {
        'author': author,
        'year_of_publication': year,
        'availability': None
    }

    action = "обновлена" if book_name in library else "добавлена"
    print(f"Книга '{book_name}' успешно {action} в библиотеке.")

def remove_book(library, book_name):
    """Удаляет книгу из библиотеки.
    Если книга не найдена выводит сообщение об этом."""
    if book_name in library:
        del library[book_name]
        print(f"Книга ' {book_name}' успешно удалена из библиотеки.")
    else:
        print(f"Книга '{book_name}' не найдена в библиотеке.")


def issue_book(library, book_name):
    """Отмечает книгу как выданную (availability = False)"""
    if book_name not in library:
        print(f"Книга '{book_name}' не найдена в библиотеке.")
        return

    if library[book_name]['availability'] is False:
        print(f"Книга '{book_name}' уже выдана.")
        return

    library[book_name]['availability'] = False
    print(f"Книга '{book_name}' успешно выдана.")


def return_book(library, book_name):
    """Отмечает книгу как возвращённую (availability = True)"""
    if book_name not in library:
        print(f"Книга '{book_name}' не найдена в библиотеке.")
        return

    if library[book_name]['availability'] is True:
        print(f"Книга '{book_name}' уже находится в библиотеке.")
        return

    library[book_name]['availability'] = True
    print(f"Книга '{book_name}' успешно возвращена в библиотеку.")


library = {}

# Добавляем книги
add_book(library, "Alice's Adventures in Wonderland", "Lewis Carroll", 1865)
add_book(library, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)

# Вывод списка книг
book_list_view(library)

# Выдаём книгу
issue_book(library, "Harry Potter and the Philosopher's Stone")

# Возвращаем книгу
return_book(library, "Harry Potter and the Philosopher's Stone")

# Пытаемся выдать несуществующую книгу
issue_book(library, "The Lord of the Rings")

# Попробуем добавить существующую книгу
add_book(library, "Harry Potter and the Philosopher's Stone", "Джоан Роулинг", 1997)

# Вывод список книг
book_list_view(library)

# Удаляем книгу
remove_book(library, "Alice's Adventures in Wonderland")

# Показываем обновлённый список
book_list_view(library)

# Попытка удалить несуществующую книгу
remove_book(library, "The Lord of the Rings")