# Shopping List Manager

shopping_list = ["milk", "bread", "eggs"]

print("Original list:")
print(shopping_list)

# Add an item
shopping_list.append("apples")

# Remove an item
shopping_list.remove("bread")

# Sort the list
shopping_list.sort()

print("\nUpdated list:")

for item in shopping_list:
    print(item)