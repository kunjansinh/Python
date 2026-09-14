def analyse_text(text):
    words = text.split()

    word_count = len(words)
    character_count = len(text)

    return word_count, character_count


message = input("Enter a sentence: ")

words, characters = analyse_text(message)

print("\n--- Text Analysis ---")
print(f"Words: {words}")
print(f"Characters: {characters}")
