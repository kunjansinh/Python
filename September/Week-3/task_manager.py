def display_tasks(tasks):
    print("\n--- Tasks ---")

    if not tasks:
        print("No tasks available.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task['title']} - {task['status']}")


tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task title: ").strip()

        if title == "":
            print("Task title cannot be empty.")
            continue

        task = {
            "title": title,
            "status": "Pending"
        }

        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        display_tasks(tasks)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
