class SmartDevice:
    def __init__(self, name, power_watts, hours_used):
        if power_watts < 0 or hours_used < 0:
            raise ValueError(
                "Power and usage hours cannot be negative."
            )

        self.name = name
        self.power_watts = power_watts
        self.hours_used = hours_used

    def calculate_energy(self):
        # Convert watt-hours to kilowatt-hours.
        return (self.power_watts * self.hours_used) / 1000

    def calculate_cost(self, price_per_kwh):
        return self.calculate_energy() * price_per_kwh

    def display_info(self, price_per_kwh):
        energy = self.calculate_energy()
        cost = self.calculate_cost(price_per_kwh)

        print(f"Device: {self.name}")
        print(f"Energy consumed: {energy:.2f} kWh")
        print(f"Energy cost: £{cost:.2f}")


class EnergyManager:
    def __init__(self, price_per_kwh):
        if price_per_kwh < 0:
            raise ValueError("Electricity price cannot be negative.")

        self.price_per_kwh = price_per_kwh
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"Added {device.name} to energy monitoring.")

    def calculate_total_energy(self):
        return sum(
            device.calculate_energy()
            for device in self.devices
        )

    def calculate_total_cost(self):
        return sum(
            device.calculate_cost(self.price_per_kwh)
            for device in self.devices
        )

    def display_report(self):
        print("\n--- Energy Consumption Report ---")

        if not self.devices:
            print("No devices have been added.")
            return

        for device in self.devices:
            device.display_info(self.price_per_kwh)
            print("-" * 25)

        print(
            f"Total energy: "
            f"{self.calculate_total_energy():.2f} kWh"
        )

        print(
            f"Total cost: "
            f"£{self.calculate_total_cost():.2f}"
        )


# Electricity price per kWh (example rate).
manager = EnergyManager(0.25)

# Create devices.
devices = [
    SmartDevice("Heater", 2000, 3),
    SmartDevice("Laptop", 65, 8),
    SmartDevice("Television", 120, 4),
    SmartDevice("Light", 10, 6)
]

# Register devices.
for device in devices:
    manager.add_device(device)

# Display report.
manager.display_report()