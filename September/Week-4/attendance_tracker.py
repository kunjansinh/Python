def calculate_attendance(attended, total_classes):
    if total_classes == 0:
        return 0

    return (attended / total_classes) * 100


students = {
    "John": [18, 20],
    "Sarah": [16, 20],
    "David": [19, 20],
    "Emma": [14, 20]
}

print("--- Attendance Report ---")

for name, data in students.items():
    attended = data[0]
    total_classes = data[1]

    percentage = calculate_attendance(attended, total_classes)

    if percentage >= 75:
        status = "Eligible"
    else:
        status = "Low Attendance"

    print(f"{name}: {percentage:.1f}% - {status}")