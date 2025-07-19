# Multiplication table:

for i in range(1, 4):
    for j in range (1, 4):
        print(f"{i} x {j}: {i} * {j} = {i * j}")
"""
1 x 1: 1 * 1 = 1
1 x 2: 1 * 2 = 2
1 x 3: 1 * 3 = 3

2 x 1: 1 * 1 = 2
2 x 2: 2 * 2 = 4
2 x 3: 2 * 3 = 6

3 x 1: 3 * 1 = 3
3 x 2: 3 * 2 = 6
3 x 3: 3 * 3 = 9
"""

number = int(input("Enter a Number: "))

for i in range(1, 13):
    for number in range(1, 13):
        print(f"{i} x {number}: {i * number}")