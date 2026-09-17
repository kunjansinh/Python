def analyse_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    return total, average


numbers = []

print("Enter numbers to analyse.")
print("Type 'done' when finished.")

while True:
    entry = input("Enter a number: ")

    if entry.lower() == "done":
        break

    try:
        number = float(entry)
        numbers.append(number)

    except ValueError:
        print("Please enter a valid number.")


if numbers:
    total, average = analyse_numbers(numbers)

    print("\n--- Number Analysis ---")
    print(f"Numbers entered: {len(numbers)}")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {max(numbers):.2f}")
    print(f"Minimum: {min(numbers):.2f}")
else:
    print("No numbers were entered.")