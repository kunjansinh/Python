# Rectangle Calculator Function


def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)

    return area, perimeter


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area, perimeter = calculate_rectangle(length, width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")