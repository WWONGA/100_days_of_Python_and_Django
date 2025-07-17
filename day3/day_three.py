# Operators

# This is the first comment
spam = 1        # and This is the second comment
                # ... and now a third comment
text = "# This is not a comment because, it is inside quotation marks."
print(spam, text)

# Numbers
a = 2 + 2   # Addition
print(a)
b = 50
c = 5 * 6   # Multiplication
print(b - c)    # 20    Subtraction
print((b - c) / a)  # 5.0   # Subtraction, then Division
print(b - c / a)    # 42.5  # Division then applied subtraction
print("Division always return a floating-point number:", 8 / 5)     # Division of any number will always return a decimal
print("17 / 3:", 17 / 3)
print("Floor division:", 17 // 3)   # No rounding-off, considers the whole number and leaves the decimals
print("Division:", 5 / 2)           # Division
print("Floor Division:", 5 // 2)     # No rounding-off, whole number only

x = 5
print("Exponentiation:", x ** 2)    # 25
a = 2
a = a ** 7  # 2 to the exponent 7 or (2 * 2 * 2 * 2 * 2 * 2 * 2) 
print(a)

length = 5  # cm
breadth = 4 # cm
area_of_rectangle = length * breadth
print("Rectangle Area:", area_of_rectangle, "cm squared")

