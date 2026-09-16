def find_largest_expense(expenses):
    if not expenses:
        return 0

    largest = expenses[0]

    for expense in expenses:
        if expense > largest:
            largest = expense

    return largest


expenses = []

print("Enter your expenses.")
print("Type 'done' when finished.")

while True:
    entry = input("Expense (£): ").lower()

    if entry == "done":
        break

    try:
        amount = float(entry)

        if amount < 0:
            print("Expense cannot be negative.")
        else:
            expenses.append(amount)

    except ValueError:
        print("Please enter a valid number.")


if expenses:
    total = sum(expenses)
    largest = find_largest_expense(expenses)

    print("\n--- Expense Summary ---")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total spent: £{total:.2f}")
    print(f"Largest expense: £{largest:.2f}")
else:
    print("No expenses entered.")