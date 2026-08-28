# Count Passing Marks


def count_passing_marks(marks):
    pass_mark = 40
    pass_count = 0

    for mark in marks:
        if mark >= pass_mark:
            pass_count = pass_count + 1

    return pass_count


marks = [35, 62, 48, 75, 81, 39, 54]

passing = count_passing_marks(marks)

print(f"Marks: {marks}")
print(f"Students who passed: {passing}")