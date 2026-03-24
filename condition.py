# 1. Сумма всех чётных чисел от 1 до 100
total_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_even += i
print("Сумма чётных чисел от 1 до 100:", total_even)
# или короче: print(sum(range(2, 101, 2)))


# 2. Список квадратов нечётных чисел от 1 до 10
odd_squares = [x**2 for x in range(1, 11, 2)]
print("Квадраты нечётных чисел от 1 до 10:", odd_squares)
# или: print("Квадраты нечётных от 1 до 10:", [x**2 for x in range(1, 11, 2)])

# 3. Подсчёт всех введённых чисел (включая отрицательное)
count = 0
print("\nВводите числа (отрицательное — стоп):")

while True:
    try:
        n = int(input("→ ").strip())
        count += 1  # считаем каждое введённое число

        if n < 0:
            break

    except ValueError:
        print("Нужно ввести целое число")

print(f"Всего введено чисел: {count}")