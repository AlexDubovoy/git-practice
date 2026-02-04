# 1. Функция, возвращающая большее из двух чисел (без использования max)
def max_number(a, b):
    return a if a > b else b

# 2. Пустая функция (используем pass)
def empty_function():
    pass

# 3. Генератор чётных чисел от 0 до n включительно
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

# 4. Автотест для функции max_number
def test_max_number():
    assert max_number(5, 3) == 5,   "5 должно быть больше 3"
    assert max_number(2, 7) == 7,   "7 должно быть больше 2"
    assert max_number(4, 4) == 4,   "при равных числах должен возвращаться любой из них"
    assert max_number(-5, -1) == -1, "−1 больше чем −5"
    assert max_number(0, 8) == 8,   "0 < 8"
    assert max_number(0, -3) == 0,  "0 больше чем −3"
    assert max_number(-100, 100) == 100, "100 больше чем −100"
    assert max_number(-10, -15) == -10,  "−10 больше чем −15"

    print("Все тесты пройдены успешно!")

# Запуск тестов при прямом запуске файла
if __name__ == "__main__":
    test_max_number()