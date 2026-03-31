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

def book_list_view(library):
    """
    Выводит названия всех книг в библиотеке.
    Если в библиотеке нет книг, функция выводит сообщение об этом.
    """
    if not library:
        print("В библиотеки нет книг.")
        return

    print("Список книг в библиотеке:")

    number = 1
    for title in library:
        print(f"{number}. {title}")
        number += 1

book_list_view(library)



