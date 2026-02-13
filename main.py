secret_password = "pass123"

while True:
    user_input = input("Введите пароль: ")

    if user_input == secret_password:
        print("Пароль верный! Добро пожаловать!")
        break
    else:
        print("Неверный пароль, попробуйте ещё раз...")