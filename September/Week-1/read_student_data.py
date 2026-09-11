def read_students():
    with open("students.txt", "r") as file:
        for line in file:
            print(line.strip())


read_students()
