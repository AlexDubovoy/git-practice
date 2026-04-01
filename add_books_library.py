def book_list_view(library):
    """Выводит названия всех книг в библиотеке.
    Если книг нет — выводит сообщение об этом."""

    if not library:
        print("В библиотеке нет книг.")
        return

    print("Список книг в библиотеке:")

    for i, book_name in enumerate(library.keys(), 1):
        print(f"{i}. {book_name}")


def add_book(book_name, author, year):
    """Добавляет новую книгу в библиотеку.
    Если книга уже существует — предлагает обновить информацию."""

    if book_name in library:
        print(f"Книга '{book_name}' уже существует в библиотеке.")
        choice = input("Хотите обновить информацию о книге? (да/нет): ").strip().lower()

        if choice != 'да':
            print("Добавление отменено.")
            return

    # Добавляем или обновляем книгу
    library[book_name] = {
        'author': author,
        'year_of_publication': year,
        'availability': None  # None = статус не определён
    }

    print(f"Книга '{book_name}' успешно добавлена/обновлена в библиотеке.")


library = {}

# Добавляем книги
add_book("Alice's Adventures in Wonderland", "Lewis Carroll", 1865)
add_book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)

# Попробуем добавить существующую книгу
add_book("Harry Potter and the Philosopher's Stone", "Джоан Роулинг", 1997)

book_list_view(library)




