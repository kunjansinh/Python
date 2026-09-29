def analyse_readings(readings, minimum, maximum):
    warnings = []

    for reading in readings:
        if reading < minimum or reading > maximum:
            warnings.append(reading)

    return warnings


readings = [22.5, 24.1, 23.8, 31.4, 21.7, 19.2, 28.6, 35.1]

minimum = 20
maximum = 30

warnings = analyse_readings(readings, minimum, maximum)

print("--- Sensor Report ---")
print(f"Total readings: {len(readings)}")
print(f"Safe range: {minimum}°C - {maximum}°C")

if warnings:
    print("\nWarning: readings outside safe range:")

    for reading in warnings:
        print(f"- {reading}°C")
else:
    print("\nAll readings are within the safe range.")
