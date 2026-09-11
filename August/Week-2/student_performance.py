# Student Performance Program

marks = [72, 45, 81, 39, 66, 54]

pass_mark = 40
pass_count = 0
fail_count = 0

for mark in marks:

    if mark >= pass_mark:
        print(f"{mark}: Pass")
        pass_count = pass_count + 1
    else:
        print(f"{mark}: Fail")
        fail_count = fail_count + 1

print()
print(f"Total students: {len(marks)}")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")