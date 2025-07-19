# Control Flow: Loops

# For loops - Iterating over sequences:
# A for loop is used to iterate over a sequence (like a list, tuple, string or range). It execute a block of code for each item in the sequence.

# Basic syntax:
"""
for item in sequence:
    code to execute for each item
"""

# 1. Iterating over a string
programming_language = "Python"
for letter in programming_language:
    print(letter)               # each letter on a new line

# 2. Iterating over a list:
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I love {fruit}")

# 3. Using range() function
# range(start, stop, step)
for i in range(5):      # 01234 each number on a new line
    print(i)

for i in range(1, 6):       #12345 each number on a new line
    print(i)

for i in range(0, 10, 2):   #02468 each number on a new line
    print(i)

# 4. Iterating with enumerate()
colours = ["red", "green", "blue"]
for wongalethu, colour in enumerate(colours):
    print(f"Index: {wongalethu}, {colour}")

# While Loops:
# A while loop will repeatedly execute a block of code as long as the condition is true.
"""
while condition:
    code to execute
    update condition to avoid infinite loop
"""
# Basic while
count = 0
while count < 5:
    print(count)
    count += 1

# 2. User input validation:
password = ""
while password != "secret":
    password = input("Enter password: ")
    print("Access granted!")
    break

# 3. Processing until condition is met:
number = 100
while number > 1:
    number = number // 2
    print(number)

# Break and Continue statements:
for i in range(10):
    if i == 5:
        break
    print(i)        # 01234

for i in range(10):
    if i % 2 != 0:      # Skip ODD numbers
        continue
    print(i)

# Break with while loop:
count = 0
while True:
    if count == 3:
        break
    print(count)
    count += 1

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)    #0124

# Else clause with Loops:
for i in range(5):
    print(i)
else:
    print("Loop completed successfully!")
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print because of break")

# While loop with else:
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While print completed!")

# Find a number
numbers =[2, 4, 6, 8, 10]
target_number = 7

for number in numbers:
    if number == target_number:
        print(f"Found {target_number}!")
        break
else:
    print(f"Target Number: {target_number} not found in the list.")

# Nested loops:
# For loop inside for loop:
for i in range(3):
    for j in range(3):
        print(f"i = {i}, j = {j}")

# Pattern Creation:
# Multiplication table:
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i} * {j} = ", i * j)
    print()     # prints empty line after each row.