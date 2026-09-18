def run_quiz(questions):
    score = 0

    for question in questions:
        print("\n" + question["question"])

        for option in question["options"]:
            print(option)

        answer = input("Your answer: ").lower()

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer was {question['answer']}.")

    return score


questions = [
    {
        "question": "What keyword is used to define a function?",
        "options": ["a) function", "b) def", "c) func"],
        "answer": "b"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["a) int", "b) str", "c) bool"],
        "answer": "c"
    },
    {
        "question": "Which symbol is used for a comment?",
        "options": ["a) //", "b) #", "c) --"],
        "answer": "b"
    }
]


score = run_quiz(questions)

print(f"\nFinal score: {score}/{len(questions)}")
