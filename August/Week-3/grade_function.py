# Grade Function


def calculate_grade(mark):
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


mark = float(input("Enter your mark: "))

grade = calculate_grade(mark)

print(f"Mark: {mark}")
print(f"Grade: {grade}")