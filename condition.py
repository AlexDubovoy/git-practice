numbers = []
current = 0

print("Вводите числа (отрицательное — стоп):")

while current >= 0:
    try:
        user_input = input("→ ").strip()
        current = int(user_input)
        numbers.append(current)
    except ValueError:
        print("Нужно ввести целое число")

print(f"Всего введено чисел: {len(numbers)}")
print("Все числа:", numbers)
