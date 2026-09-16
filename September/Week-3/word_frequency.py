def count_words(sentence):
    words = sentence.lower().split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


sentence = input("Enter a sentence: ")

result = count_words(sentence)

print("\n--- Word Frequency ---")

for word, count in result.items():
    print(f"{word}: {count}")