# Find first even number:
numbers = [1, 3, 7, 9, 8, 5, 2]
for even_number in numbers:
    if even_number % 2 == 0:
        print(f"First even number found: {even_number}")
        break