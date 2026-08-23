# Number Statistics

numbers = [15, 8, 23, 42, 11, 30]

total = 0
even_count = 0
odd_count = 0

for number in numbers:
    total = total + number

    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

average = total / len(numbers)

print(f"Numbers: {numbers}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")