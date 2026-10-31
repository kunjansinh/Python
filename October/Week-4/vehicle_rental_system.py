class Vehicle:
    def __init__(self, vehicle_id, brand, daily_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.__daily_rate = daily_rate

    def calculate_rental(self, days):
        if days <= 0:
            raise ValueError("Rental days must be positive.")

        return self.__daily_rate * days

    def display_info(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, daily_rate, seats):
        super().__init__(vehicle_id, brand, daily_rate)
        self.seats = seats

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        return base_cost + 15 * days


class Motorbike(Vehicle):
    def __init__(self, vehicle_id, brand, daily_rate, engine_cc):
        super().__init__(vehicle_id, brand, daily_rate)
        self.engine_cc = engine_cc

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        return base_cost + 5 * days


def display_rental(vehicle, days):
    vehicle.display_info()
    cost = vehicle.calculate_rental(days)
    print(f"Rental duration: {days} days")
    print(f"Total rental cost: £{cost:.2f}")
    print("-" * 30)


# Create vehicles
vehicles = [
    Car("C101", "Toyota", 40, 5),
    Motorbike("M201", "Honda", 20, 150)
]

# Calculate rental costs
for vehicle in vehicles:
    display_rental(vehicle, 3)

# Test invalid input
try:
    vehicles[0].calculate_rental(-2)
except ValueError as error:
    print(f"Error: {error}")