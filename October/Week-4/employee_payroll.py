
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        return 0

    def display_details(self):
        print(f"Employee: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: £{self.calculate_salary():.2f}")


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Create employee objects
employees = [
    FullTimeEmployee("Alex", "E101", 2500),
    PartTimeEmployee("Sam", "E102", 12.50, 60),
    PartTimeEmployee("Jordan", "E103", 15, 40)
]

# Display each employee's details
for employee in employees:
    employee.display_details()
    print("-" * 30)