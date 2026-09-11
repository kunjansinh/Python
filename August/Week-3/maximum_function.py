# Maximum Number Function


def find_maximum(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


numbers = [15, 42, 8, 27, 63, 19]

maximum = find_maximum(numbers)

print(f"Numbers: {numbers}")
print(f"Maximum number: {maximum}")