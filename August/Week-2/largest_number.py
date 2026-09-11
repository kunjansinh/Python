# Find the Largest Number

numbers = [12, 45, 7, 89, 34, 23]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"Largest number: {largest}")