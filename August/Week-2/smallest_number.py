# Find the Smallest Number

numbers = [25, 12, 47, 8, 31, 19]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(f"Numbers: {numbers}")
print(f"Smallest number: {smallest}")