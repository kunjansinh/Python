def display_results(votes):
    print("\n=== POLL RESULTS ===")

    total_votes = sum(votes.values())

    if total_votes == 0:
        print("No votes have been recorded.")
        return

    for language, count in votes.items():
        percentage = (count / total_votes) * 100

        print(
            f"{language}: {count} vote(s) "
            f"({percentage:.1f}%)"
        )

    highest_votes = max(votes.values())

    winners = [
        language
        for language, count in votes.items()
        if count == highest_votes
    ]

    if len(winners) == 1:
        print(f"\nWinner: {winners[0]}")
    else:
        print(f"\nIt's a tie between: {', '.join(winners)}")

    print(f"Total votes: {total_votes}")


def run_poll():
    votes = {
        "Python": 0,
        "Java": 0,
        "C++": 0,
        "JavaScript": 0
    }

    while True:
        print("\n=== PROGRAMMING LANGUAGE POLL ===")

        for number, language in enumerate(votes, start=1):
            print(f"{number}. {language}")

        print("5. Show results and exit")

        choice = input("Cast your vote: ").strip()

        if choice == "5":
            break

        try:
            choice_number = int(choice)

            languages = list(votes.keys())

            if 1 <= choice_number <= len(languages):
                selected_language = languages[choice_number - 1]
                votes[selected_language] += 1

                print(f"Your vote for {selected_language} was recorded.")

            else:
                print("Please select a valid option.")

        except ValueError:
            print("Enter a number between 1 and 5.")

    display_results(votes)


run_poll()