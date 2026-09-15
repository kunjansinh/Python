def calculate_total(prices):
    return sum(prices)


budget = float(input("Enter your budget: "))

prices = []

while True:
    entry = input("Enter item price or type 'done': ").lower()

    if entry == "done":
        break

    try:
        price = float(entry)

        if price < 0:
            print("Price cannot be negative.")
        else:
            prices.append(price)

    except ValueError:
        print("Please enter a valid price.")


total = calculate_total(prices)
remaining = budget - total

print("\n--- Shopping Summary ---")
print(f"Items entered: {len(prices)}")
print(f"Total: £{total:.2f}")

if remaining >= 0:
    print(f"Remaining budget: £{remaining:.2f}")
else:
    print(f"Over budget by: £{-remaining:.2f}")
