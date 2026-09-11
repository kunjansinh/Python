# Count Passing Marks

marks = [35, 62, 48, 75, 81, 39, 54]

pass_mark = 40
pass_count = 0

for mark in marks:
    if mark >= pass_mark:
        pass_count = pass_count + 1

print(f"Marks: {marks}")
print(f"Number of students who passed: {pass_count}")