print("Welcome to day 2: ")

# Arithmetic
print("40 + 2 =", 40 + 2)
print("43 - 1 =", 43 - 1)
print("6 * 7 = ", 6 * 7)
print("84 / 2 =", 84 / 2)
print("6 ** 2 + 6 =", 6 ** 2 + 6 )

# Values and Types:
print("This is a: ", type(2))      # Integer
print("This is a:", type(42.0))   # Floating-point number
print("This is a:", type("Anything inside Quotation marks is: "))     # String
print("This is a:", type(False))    # Boolean

# Variables and values:
message = "Hello, World!"
print("Displaying the value of message:", message)
n = 17
print("The value of 'n': " + str(n))
pi = 3.141592
print("This is the mathematical value of 'pi'", pi)

# 10_percent = 0.1        # syntax error, variable names don't start with numbers
_20_percent = 0.2       # valid variable name
n += 25     # n = (n + 25)
print("Updated value of n: " + str(n))

print(5 * "spam")

## Data types:
# Integer:
a = 2
print(a)    # 2
print(f"Data type of a: {a} is: {type(a)}")

b = 9223372036854775807
print(f"b is: {b} and of type: {type(b)}")      # f-string formatting

# Floating point
pi = 3.14
print(f"pi: {pi} and is of type: {type(pi)}")

# String
c = "A"
print(f"The type c: {type(c)}, while value of c is: {c}")
name = "Wongalethu Jezile"
print(f"My fullname is: {name}")

# Boolean
q = True
print(q)

# Empty value or null data type
X = None
print(f"The value of X is: {X}, and its type is: {type(X)} ")

a, b, c = 1, 2, 3
print(f"The values of a, b and c are respectively: {a, b, c} and their SUM is: {a + b + c}")

a = b = c = 1
print(a, b, c)

b = 2
print(a, b, c)      # b is now 2.

x = y = [7, 8, 9]
print(x, y)

x[0] = 13

print(x, y)     # x has updated to: (13, 8, 9), y has the updated value of x
x = [1, 2, [3, 4, 5], 6, 7]     # This is a list within a list #NESTED LIST
print(x[2])     #[3, 4, 5]
