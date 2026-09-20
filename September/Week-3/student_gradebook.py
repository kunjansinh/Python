def calculate_average(marks):
    if not marks:
        return 0

    return sum(marks) / len(marks)


students = {
    "John": [65, 72, 81],
    "Sarah": [82, 90, 76],
    "David": [58, 64, 61]
}

print("--- Student Gradebook ---")

for name, marks in students.items():
    average = calculate_average(marks)

    print(f"{name}:")
    print(f"  Marks: {marks}")
    print(f"  Average: {average:.2f}")
