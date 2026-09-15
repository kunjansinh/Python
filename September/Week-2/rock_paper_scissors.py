import random


def decide_winner(player, computer):
    if player == computer:
        return "It's a draw!"

    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "You win!"

    return "Computer wins!"


choices = ["rock", "paper", "scissors"]

player_choice = input("Choose rock, paper, or scissors: ").lower()

if player_choice not in choices:
    print("Invalid choice.")
else:
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")
    print(decide_winner(player_choice, computer_choice))
