def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return sorted(duplicates)

numbers = [4, 7, 2, 4, 9, 7, 4, 3, 2, 10]

duplicates = find_duplicates(numbers)

print("Original numbers:", numbers)

if duplicates:
    print("Duplicate numbers:", duplicates)
else:
    print("No duplicates found.")