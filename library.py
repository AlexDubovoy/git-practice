def book_list_view(library):
    """Выводит названия всех книг в библиотеке.
    Если книг нет — выводит сообщение об этом."""

    if not library:
        print("В библиотеке нет книг.")
        return

    print("Список книг в библиотеке:")

    for i, title in enumerate(library.keys(), 1):
        print(f"{i}. {title}")


library = {
    "Alice's Adventures in Wonderland": {
        'author': 'Lewis Carroll',
        'year_of_publication': 1865,
        'availability': True
    },
    "Harry Potter and the Philosopher's Stone": {
        'author': 'J.K. Rowling',
        'year_of_publication': 1997,
        'availability': False
    }
}

book_list_view(library)