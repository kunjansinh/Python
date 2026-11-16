from collections import Counter
import string


def top_words(text: str, limit: int = 5) -> list[tuple[str, int]]:
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.lower().translate(translator)
    words = cleaned_text.split()
    return Counter(words).most_common(limit)


if __name__ == "__main__":
    sample_text = (
        "Python is simple, readable, and powerful. "
        "Many developers choose Python because clean code is easy to write."
    )
    for word, count in top_words(sample_text, limit=3):
        print(f"{word}: {count}")