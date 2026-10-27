class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.__is_on = False
        print(f"{self.name} is now OFF.")

    def get_status(self):
        return "ON" if self.__is_on else "OFF"

    def display_info(self):
        print(f"{self.name}: {self.get_status()}")


class SmartLight(SmartDevice):
    def __init__(self, name, brightness=50):
        super().__init__(name)
        self.brightness = brightness

    def set_brightness(self, brightness):
        if not 0 <= brightness <= 100:
            raise ValueError(
                "Brightness must be between 0 and 100."
            )

        self.brightness = brightness
        print(
            f"{self.name} brightness set to "
            f"{self.brightness}%."
        )

    def display_info(self):
        super().display_info()
        print(f"Brightness: {self.brightness}%")


class SmartFan(SmartDevice):
    def __init__(self, name, speed=1):
        super().__init__(name)
        self.speed = speed

    def set_speed(self, speed):
        if speed not in (1, 2, 3):
            raise ValueError(
                "Fan speed must be 1, 2, or 3."
            )

        self.speed = speed
        print(f"{self.name} speed set to {self.speed}.")


# Create devices
devices = [
    SmartLight("Living Room Light", 70),
    SmartFan("Bedroom Fan", 2)
]

# Turn on every device
for device in devices:
    device.turn_on()

print("\n--- Device Information ---")

# Polymorphism: each object can display its own information
for device in devices:
    device.display_info()
    print()

# Change settings with exception handling
try:
    devices[0].set_brightness(85)
    devices[1].set_speed(5)
except ValueError as error:
    print(f"Invalid setting: {error}")

print("\n--- Final Device Status ---")

for device in devices:
    device.display_info()