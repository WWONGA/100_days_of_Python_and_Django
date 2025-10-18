# Exercises:

"""
🧠Exercises

1. Write a program that:
    Takes two numbers as input.
    Prints all arithmetic operations (addition, subtraction, multiplication, division).

2. Create a program that compares two numbers and tells which one is greater, or if they are equal.

3. Use logical operators to check:
    If a number is between 10 and 50.
    If a name starts with “A” or ends with “n”.

4. Test membership:
    Create a list of your 5 favorite colours.
    Check if “blue” and “black” are in the list.
    
5. Use assignment operators to double and then reduce a number.

"""

# Two numbers as input:
# Arithmetic (Addition, Subtraction, Multiplication and Division)

number_one = int(input("Enter a number: "))
number_two = int(input("Enter a number: "))

print(f"Addition: {number_one + number_two}")
print(f"Subtraction: {number_one - number_two}")
print(f"Multiplication: {number_one * number_two}")
print(f"Division: {number_one / number_two}")

# Program compares two numbers:
# Which one is greater and if they are equal

c = 20
d = 10
print(f"Greater and Equal to: {c} is Greater than {d}: {c >= d}")       # True

# Use logical operators to check: (and, or AND not)
"""
If a number is between 10 and 50.
If a name starts with “A” or ends with “n”.
"""

number_check = 21
print(10 < number_check and number_check< 50)   # True
name = "American"
letters_check = name.startswith("A") or name.endswith("n")
print(letters_check)

# Test membership:
# Check if “blue” and “black” are in the list.
favourite_colours = ["blue", "black", "white", "pink", "navy"]
print("blue" in favourite_colours and "black" in favourite_colours)

# Assignment operators:
# double and then reduce a number

number_double_reduce = 5
number_double_reduce *= 2
number_double_reduce -= 3
print(number_double_reduce)