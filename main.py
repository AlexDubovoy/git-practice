age = int(input("Введите ваш возраст: "))
citizenship = input("Вы гражданин страны? (да/нет): ").lower() == "да"
criminal_record = input("Есть ли у вас 120судимость? (да/нет): ").lower() == "да"

if age >= 18 and citizenship and not criminal_record:
    print("Вы можете голосовать!")
else:
    print("Голосовать нельзя.")
