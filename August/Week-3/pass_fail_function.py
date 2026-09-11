# Pass or Fail Function


def check_result(mark):
    if mark >= 40:
        return "Pass"
    else:
        return "Fail"


mark = float(input("Enter your mark: "))

result = check_result(mark)

print(f"Result: {result}")