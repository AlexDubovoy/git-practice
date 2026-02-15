text = input("Текст: ").lower()

# убираем знаки препинания и пробелы
for p in ".,!?;:-—()\"'«»…":
    text = text.replace(p, " ")

words = text.split()

if not words:
    print("Нет слов")
else:
    # 1. количество слов
    print("Слов:", len(words))

    # 2. самое длинное слово
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    print("Самое длинное:", longest)

    # 3. гласные
    count = 0
    for c in text:
        if c in "аеёиоуыэюя":
            count += 1
    print("Гласных:", count)

    # 4. частота слов
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1

    print("\nЧастота:")
    for w in count:
        print(w, "→", count[w])
