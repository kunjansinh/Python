# Number List Manager

numbers = [15, 4, 23, 8, 42]

print(f"Original list: {numbers}")

# Add a number
numbers.append(30)

# Remove a number
numbers.remove(4)

# Sort the list
numbers.sort()

print(f"Updated list: {numbers}")

print("Numbers greater than 20:")

for number in numbers:
    if number > 20:
        print(number)