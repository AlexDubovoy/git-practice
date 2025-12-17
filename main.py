while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operations = input("Введите знак операции (+, -, *, /) или 'q' для выхода: ")

        if operations == 'q':
            print("Выход из программы.")
        break

        if operations == '+':
            print(f"Результат сложения: {num1 + num2}")
        elif operations == '-':
            print(f"Результат вычитания: {num1 - num2}")
        elif operations == '*':
            print(f"Результат умножения: {num1 * num2}")
        elif operations == '/':
            if num2 == 0:
                print("Ошибка: Деление на ноль запрещено.")
            else:
                print(f"Результат деления: {num1 / num2}")
        else:
            print("Ошибка: Неверная операция. Используйте +, -, *, /.")
    except ValueError:
        print("Ошибка: Это не число! Пожалуйста, введите число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("--- Операция завершена ---\n") #выход




