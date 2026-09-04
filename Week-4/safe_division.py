# Safe Division


def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return None


numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

result = divide_numbers(numerator, denominator)

if result is None:
    print("Error: Cannot divide by zero.")
else:
    print(f"Result: {result}")