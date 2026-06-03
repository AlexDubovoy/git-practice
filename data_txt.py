with open('data.txt', 'w', encoding='utf-8') as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)

with open('data.txt', 'a', encoding='utf-8') as file:
    file.write("Четвёртая строка\n")
    file.write("Пятая строка\n")

with open('data.txt', 'r', encoding='utf-8') as file:
    print("\nСодержимое файла построчно:")
    for line in file:
        print(line.strip())

with open('data.txt', 'rb') as source_file:
    with open('data_copy.txt', 'wb') as copy_file:
        copy_file.write(source_file.read())
print("\nФайл скопирован в data_copy.txt")

