def clean_and_split(text: str) -> list[str]:
    text = text.lower()
    for p in ".,!?;:-—()\"'«»…":
        text = text.replace(p, " ")
    return text.split()


def longest_word(words: list[str]) -> str:
    return max(words, key=len) if words else ""


def vowel_count(text: str) -> int:
    return sum(1 for c in text if c in "аеёиоуыэюя")


def word_freq(words: list[str]) -> dict:
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


text = input("Текст: ").strip()
words = clean_and_split(text)

if not words:
    print("Нет слов")
else:
    print("Слов:", len(words))
    print("Самое длинное:", longest_word(words))
    print("Гласных:", vowel_count(" ".join(words)))
    print("\nЧастота:")
    for w, cnt in sorted(word_freq(words).items()):
        print(f"{w:20} {cnt}")