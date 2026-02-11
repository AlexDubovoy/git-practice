while True:
    entering_numbers = input("Введите целое положительное число: ").strip()

    if entering_numbers.isdigit():
        n = int(entering_numbers)
        break
    else:
        print("Пожалуйста, введите целое положительное число")

print("Начало отчёта:")
while n >= 0:
    print(n)
    n -= 1

print("Отсчёт завершён.")