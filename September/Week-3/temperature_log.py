def check_temperature(temperature):
    if temperature < 10:
        return "LOW"

    elif temperature > 30:
        return "HIGH"

    return "NORMAL"


temperatures = [18.5, 21.0, 27.3, 32.1, 8.7, 24.6]

print("--- Temperature Monitor ---")

for temperature in temperatures:
    status = check_temperature(temperature)

    print(f"Temperature: {temperature:.1f}°C | Status: {status}")