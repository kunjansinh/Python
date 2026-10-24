class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(
            f"{self.name}: "
            f"£{self.price:.2f} | "
            f"Stock: {self.quantity}"
        )

    def stock_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_inventory(self):
        print("\n--- Inventory ---")

        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            product.display()

    def calculate_total_value(self):
        total = 0

        for product in self.products:
            total += product.stock_value()

        return total


inventory = Inventory()

inventory.add_product(Product("Keyboard", 25.99, 10))
inventory.add_product(Product("Mouse", 12.50, 15))
inventory.add_product(Product("Monitor", 149.99, 4))

inventory.display_inventory()

total_value = inventory.calculate_total_value()

print(f"\nTotal inventory value: £{total_value:.2f}")