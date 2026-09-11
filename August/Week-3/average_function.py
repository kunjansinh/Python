# Average Function


def calculate_average(numbers):
    total = 0

    for number in numbers:
        total = total + number

    average = total / len(numbers)

    return average


marks = [65, 72, 48, 81, 56]

average = calculate_average(marks)

print(f"Marks: {marks}")
print(f"Average: {average:.2f}")