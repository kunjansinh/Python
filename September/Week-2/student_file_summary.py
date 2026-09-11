def count_students(filename):
    count = 0

    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                count += 1

    return count


number_of_students = count_students("students.txt")

print(f"Number of students: {number_of_students}")