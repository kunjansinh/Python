def check_system_health(cpu_temperature, memory_usage, battery_level):
    alerts = []

    if cpu_temperature > 80:
        alerts.append("High CPU temperature")

    if memory_usage > 85:
        alerts.append("High memory usage")

    if battery_level < 20:
        alerts.append("Low battery")

    return alerts


def display_report(readings):
    print("\n========== SYSTEM HEALTH REPORT ==========")

    for system_name, values in readings.items():
        print(f"\nSystem: {system_name}")
        print(f"CPU temperature: {values['cpu']}°C")
        print(f"Memory usage: {values['memory']}%")
        print(f"Battery level: {values['battery']}%")

        alerts = check_system_health(
            values["cpu"],
            values["memory"],
            values["battery"]
        )

        if alerts:
            print("Status: WARNING")

            for alert in alerts:
                print(f"- {alert}")
        else:
            print("Status: HEALTHY")


readings = {
    "Device A": {"cpu": 65, "memory": 70, "battery": 80},
    "Device B": {"cpu": 92, "memory": 90, "battery": 15},
    "Device C": {"cpu": 72, "memory": 60, "battery": 45}
}

display_report(readings)