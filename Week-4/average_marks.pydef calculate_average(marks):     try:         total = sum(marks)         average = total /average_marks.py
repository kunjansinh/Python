def calculate_average(marks):
    try:
        total = sum(marks)
        average = total / len(marks)
        return average
    except ZeroDivisionError:
        return None


marks = [65, 72, 81, 59, 74]

average = calculate_average(marks)

if average is None:
    print("No marks were provided.")
else:
    print(f"Average mark: {average:.2f}")
