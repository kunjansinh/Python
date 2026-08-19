# Calculate Total and Average

marks = [65, 72, 48, 81, 56]

total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")