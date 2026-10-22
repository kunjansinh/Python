def calculate_average(scores):
    if not scores:
        return 0

    return sum(scores) / len(scores)


def count_passes(scores, pass_mark):
    passed = 0

    for score in scores:
        if score >= pass_mark:
            passed += 1

    return passed


def get_grade(average):
    if average >= 70:
        return "Distinction"
    elif average >= 60:
        return "Merit"
    elif average >= 40:
        return "Pass"
    else:
        return "Needs Improvement"


scores = []

print("=== QUIZ SCORE ANALYSER ===")
print("Enter scores between 0 and 100.")
print("Type 'done' when finished.")

while True:
    entry = input("Enter quiz score: ").strip().lower()

    if entry == "done":
        break

    try:
        score = float(entry)

        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("Score must be between 0 and 100.")

    except ValueError:
        print("Please enter a valid number.")


if scores:
    average = calculate_average(scores)
    passed = count_passes(scores, 40)

    print("\n=== PERFORMANCE REPORT ===")
    print(f"Number of quizzes: {len(scores)}")
    print(f"Scores: {scores}")
    print(f"Average score: {average:.2f}")
    print(f"Highest score: {max(scores):.2f}")
    print(f"Lowest score: {min(scores):.2f}")
    print(f"Quizzes passed: {passed}")
    print(f"Quizzes failed: {len(scores) - passed}")
    print(f"Overall grade: {get_grade(average)}")
else:
    print("No scores were entered.")