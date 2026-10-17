def display_goals(goals):
    print("\n========== DAILY GOALS ==========")

    if not goals:
        print("You haven't added any goals yet.")
        return

    for number, goal in enumerate(goals, start=1):
        status = "Completed" if goal["completed"] else "Pending"
        print(f"{number}. {goal['title']} - {status}")

    completed = sum(1 for goal in goals if goal["completed"])
    total = len(goals)
    percentage = (completed / total) * 100

    print("---------------------------------")
    print(f"Progress: {completed}/{total} goals")
    print(f"Completion rate: {percentage:.1f}%")


def add_goal(goals):
    title = input("Enter your goal: ").strip()

    if not title:
        print("Goal cannot be empty.")
        return

    goals.append({
        "title": title,
        "completed": False
    })

    print("Goal added successfully!")


def complete_goal(goals):
    if not goals:
        print("There are no goals to complete.")
        return

    display_goals(goals)

    try:
        number = int(input("Enter the goal number to complete: "))

        if 1 <= number <= len(goals):
            goal = goals[number - 1]

            if goal["completed"]:
                print("This goal is already completed.")
            else:
                goal["completed"] = True
                print(f"Completed: {goal['title']}")

        else:
            print("Invalid goal number.")

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    goals = []

    while True:
        print("\n========== GOAL TRACKER ==========")
        print("1. Add a goal")
        print("2. View goals")
        print("3. Complete a goal")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_goal(goals)

        elif choice == "2":
            display_goals(goals)

        elif choice == "3":
            complete_goal(goals)

        elif choice == "4":
            print("Keep working towards your goals!")
            break

        else:
            print("Invalid option. Choose 1-4.")


if __name__ == "__main__":
    main()