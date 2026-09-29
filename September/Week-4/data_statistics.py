def calculate_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    highest = numbers[0]
    lowest = numbers[0]

    for number in numbers:
        if number > highest:
            highest = number

        if number < lowest:
            lowest = number

    return total, average, highest, lowest


numbers = [12, 18, 7, 25, 14, 31, 9, 20]

total, average, highest, lowest = calculate_statistics(numbers)

print("--- Data Statistics ---")
print(f"Data points: {len(numbers)}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
