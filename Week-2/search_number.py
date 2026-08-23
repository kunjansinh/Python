# Search for a Number

numbers = [12, 25, 7, 34, 18, 42]

search_number = int(input("Enter a number to search for: "))

found = False

for number in numbers:
    if number == search_number:
        found = True
        break

if found:
    print(f"{search_number} was found in the list.")
else:
    print(f"{search_number} was not found in the list.")