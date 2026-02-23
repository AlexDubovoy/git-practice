# 1. Сумма чётных от 1 до 100
print("Сумма чётных от 1 до 100:", sum(range(2, 101, 2)))

# 2. Квадраты нечётных от 1 до 10
print("Квадраты нечётных 1 до 10:", [x**2 for x in range(1, 11, 2)])

# 3. Счётчик чисел до отрицательного
count = 0
print("Вводите числа (отрицательное — стоп):")

number = 0

while number >= 0:
    try:
        enter = input("→ ").strip()
        number = int(enter)
        if number >= 0:
            count += 1
    except ValueError:
        print("Нужно ввести целое число")

print(f"Введено неотрицательных чисел: {count}")