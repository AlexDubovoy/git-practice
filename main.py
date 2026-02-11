while True:
    try:
        n = int(input("Введите целое положительное число: ").strip())
        if n >= 0:
            break
        print("Число должно быть неотрицательным")
    except ValueError:
        print("Нужно ввести целое число")

print("Начало отсчёта:")
while n >= 0:
    print(n)
    n -= 1

print("Отсчёт завершён.")