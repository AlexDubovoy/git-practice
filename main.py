while True:
    try:
        age = int(input("Введите ваш возраст: ").strip())
        break
    except ValueError:
        print("Пожалуйста, введите число (возраст).")

citizenship = input("Вы гражданин страны? (да/нет): ").strip().lower() == "да"
criminal_record = input("Есть ли судимость? (да/нет): ").strip().lower() == "да"

if age >= 18 and citizenship and not criminal_record:
    print("Вы можете голосовать!")
else:
    print("Голосовать нельзя.")
