import random


def display_word(word, guessed_letters):
    displayed_word = ""

    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    return displayed_word.strip()


def play_game():
    words = ["python", "computer", "programming", "keyboard", "developer"]

    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 8

    print("=== WORD GUESSING GAME ===")
    print("Guess the hidden word one letter at a time!")

    while attempts_left > 0:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print(f"Attempts remaining: {attempts_left}")

        guess = input("Enter one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct! That letter is in the word.")
        else:
            attempts_left -= 1
            print("Incorrect! Try another letter.")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed '{secret_word}'.")
            return

    print(f"\nGame over! The word was '{secret_word}'.")


play_game()