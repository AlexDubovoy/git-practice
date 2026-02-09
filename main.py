while True:
    entering_numbers = input("Введите число от 1 до 5: ").strip()

    if not entering_numbers.isdigit():
        print("Пожалуйста, введите число (цифру)")
        continue

    n = int(entering_numbers)

    if 1 <= n <= 5:
        words = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
        print("Соответствующее слово:", words[n])
        break
    else:
        print("Число должно быть от 1 до 5 включительно")