def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("--- Temperature Converter ---")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose an option: ")

try:
    temperature = float(input("Enter temperature: "))

    if choice == "1":
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature:.1f}°C = {result:.1f}°F")

    elif choice == "2":
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature:.1f}°F = {result:.1f}°C")

    else:
        print("Invalid option.")

except ValueError:
    print("Please enter a valid number.")
