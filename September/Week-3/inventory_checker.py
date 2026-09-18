def check_inventory(inventory):
    for item, quantity in inventory.items():
        if quantity == 0:
            print(f"{item}: OUT OF STOCK")
        elif quantity < 5:
            print(f"{item}: LOW STOCK ({quantity})")
        else:
            print(f"{item}: {quantity} available")


inventory = {
    "Rice": 12,
    "Masala": 4,
    "Biscuits": 8,
    "Tea": 0,
    "Lentils": 3
}

print("--- Inventory Report ---")
check_inventory(inventory)
