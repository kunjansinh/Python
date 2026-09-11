def add_student(name, mark):
    with open("students.txt", "a") as file:
        file.write(f"{name} - {mark}\n")


add_student("Alex", 78)

print("Student added successfully.")
