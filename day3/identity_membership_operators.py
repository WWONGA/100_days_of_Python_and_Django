"""Identity and
Membership Operators
"""

# Identity
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True (same the same object)
print(a is c)       # False (different object which happens to have same values)
print(a is not c)   # True (the just share or have the same values)

# Membership
numbers = [10, 20, 30]
print(20 in numbers)        # True 20 is in the list(numbers)
print(50 not in numbers)    # True 50 is not in the list(numbers)

# Example 1: (Arithmetic and Comparison)
a = 15
b = 4
print("Sum:", a + b)        # Arithmetic (19)
print("a > b:", a > b)      # Comparison (True)

# Example 2: (Logical Operator)
is_adult = True
has_id = False
print(is_adult and has_id)      # False

# Example 3: (Membership)
word = "python"
print("y" in word)      # True
print("z" not in word)  # True
