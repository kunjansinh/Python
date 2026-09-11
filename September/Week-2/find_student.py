def find_student(name):
    with open("students.txt", "r") as file:
        for line in file:
            if name.lower() in line.lower():
                return line.strip()

    return None


student_name = input("Enter student name: ")

result = find_student(student_name)

if result is None:
    print("Student not found.")
else:
    print(f"Student found: {result}")