import time


def calculate_accuracy(original, typed):
    if not typed:
        return 0.0

    correct_characters = 0

    for index, character in enumerate(typed):
        if index < len(original) and character == original[index]:
            correct_characters += 1

    accuracy = (correct_characters / len(typed)) * 100

    return accuracy


def run_typing_test():
    sentence = (
        "Python makes it possible to solve problems "
        "with simple and reusable code"
    )

    print("\n========== TYPING SPEED TEST ==========")
    print("\nType the following sentence as accurately as possible:\n")
    print(sentence)

    input("\nPress Enter when you are ready to start...")

    start_time = time.perf_counter()

    typed_text = input("\nStart typing: ")

    end_time = time.perf_counter()

    elapsed_seconds = end_time - start_time

    if elapsed_seconds <= 0:
        print("Unable to calculate typing speed.")
        return

    typed_words = len(typed_text.split())
    elapsed_minutes = elapsed_seconds / 60

    words_per_minute = typed_words / elapsed_minutes

    accuracy = calculate_accuracy(sentence, typed_text)

    print("\n========== YOUR RESULTS ==========")
    print(f"Time taken: {elapsed_seconds:.2f} seconds")
    print(f"Words typed: {typed_words}")
    print(f"Typing speed: {words_per_minute:.1f} WPM")
    print(f"Typing accuracy: {accuracy:.1f}%")

    if accuracy >= 95:
        print("Excellent accuracy!")
    elif accuracy >= 80:
        print("Good effort! Keep practising.")
    else:
        print("Focus on accuracy before increasing speed.")


if __name__ == "__main__":
    run_typing_test()