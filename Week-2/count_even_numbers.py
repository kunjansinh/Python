# Count Even Numbers

numbers = [4, 7, 12, 15, 20, 23, 30]

even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count = even_count + 1

print(f"Numbers in the list: {numbers}")
print(f"Number of even values: {even_count}")