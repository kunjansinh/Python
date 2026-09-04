def calculate_average(marks):
    return sum(marks) / len(marks)


# Write marks to a file
file = open("marks.txt", "w")

file.write("65\n")
file.write("72\n")
file.write("81\n")
file.write("59\n")
file.write("74\n")

file.close()


# Read marks from the file
marks = []

file = open("marks.txt", "r")

for line in file:
    mark = float(line.strip())
    marks.append(mark)

file.close()


# Calculate and display the average
average = calculate_average(marks)

print("Marks:", marks)
print(f"Average: {average:.2f}")
