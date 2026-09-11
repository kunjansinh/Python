students = 
[
    "John - 75",
    "Sarah - 82",
    "David - 68",
    "Emma - 91"
]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("Student data saved successfully.")
