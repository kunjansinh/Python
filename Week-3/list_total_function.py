# Calculate List Total


def calculate_total(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


numbers = [10, 25, 15, 30, 20]

total = calculate_total(numbers)

print(f"Numbers: {numbers}")
print(f"Total: {total}")