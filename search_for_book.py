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


def find_book(library, book_name):
    """Выводит полную информацию о книге по названию.
    Также показывает статус наличия книги с разными сообщениями."""
    if book_name not in library:
        print(f"Книга '{book_name}' не найдена в библиотеке.")
        return

    book = library[book_name]

    if book['availability'] is None:
        status_message = "Книга в библиотеке (статус не определён)."
    elif book['availability'] is False:
        status_message = "Книга выдана"
    else:
        status_message = "Книга в наличии"


    print(f"\nИнформация о книге '{book_name}':")
    print(f"Автор: {book['author']}")
    print(f"Год издания: {book['year_of_publication']}")
    print(f"Статус: {status_message}")


library = {}

# 1. Добавление книг
print("\n1. Добавление книг:")
add_book(library, "Alice's Adventures in Wonderland", "Lewis Carroll", 1865)
add_book(library, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
add_book(library, "1984", "George Orwell", 1949)
add_book(library, "To Kill a Mockingbird", "Harper Lee", 1960)
add_book(library, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
add_book(library, "The Hobbit", "J.R.R. Tolkien", 1937)
add_book(library, "Brave New World", "Aldous Huxley", 1932)

# 2. Просмотр списка книг
book_list_view(library)

# 3. Выдача книги
print("\n3. Выдача книги:")
issue_book(library, "Harry Potter and the Philosopher's Stone")

# 4. Возврат книги
print("\n4. Возврат книги:")
return_book(library, "Harry Potter and the Philosopher's Stone")

# 5. Попытка выдать несуществующую книгу
print("\n5. Попытка выдать несуществующую книгу:")
issue_book(library, "The Lord of the Rings")

# 6. Обновление существующей книги
print("\n6. Обновление информации о существующей книге:")
add_book(library, "Harry Potter and the Philosopher's Stone", "Джоан Роулинг", 1997)

# 7. Просмотр обновлённого списка
book_list_view(library)

# 8. Удаление книги
print("\n8. Удаление книги:")
remove_book(library, "Alice's Adventures in Wonderland")

# 9. Финальный просмотр списка
book_list_view(library)

# 10. Поиск книг
print("\n10. Поиск книг:")
find_book(library, "Harry Potter and the Philosopher's Stone")
find_book(library, "Alice's Adventures in Wonderland")
find_book(library, "Pride and Prejudice")