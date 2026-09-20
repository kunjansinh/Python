def count_numbers(numbers):
    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    return frequency


numbers = [4, 2, 4, 7, 2, 4, 9, 7, 2, 4]

result = count_numbers(numbers)

print("--- Number Frequency ---")

for number, count in result.items():
    print(f"{number}: {count} time(s)")
