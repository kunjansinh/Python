# Calculator Function


def calculate_area(length, width):
    area = length * width
    return area


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = calculate_area(length, width)

print(f"Rectangle area: {area}")