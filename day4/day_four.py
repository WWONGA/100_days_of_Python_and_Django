# Conditional Statements:

# if-statement
"""
if condition:
    code to execute/run if condition is True
    statement1
    statement2
    ...
"""
age = 18
if age >= 18:
    print("You are an adult!")

# if-else statement:
"""
if condition:
    code to execute if condition is True
else:
    code to run if condition is False
"""

temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant!")

# else-if Statements
"""
if condition1
    code to run if condition1 is True
elif condition2
    code to execute if condition2 is True
elif condition3
    code to run if condition3 is True
else:
    code to run if none of the above conditions are met (True)
"""

score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

# Nested conditionals:
age = 17
has_licence = True

if age >= 18:
    if has_licence:
        print("You can drive!")
    else:
        print("You need a licence to drive!")
else:
    print("You are too young to drive!")

# The ternary operator:
# display VALUE if_VALUE_True if condition else condition display VALUE if_VALUE_False
age = 37
status = "adult" if age >= 18 else "minor"
print(f"You are a {status}")

# Combining Conditions (using "and", "or" AND "not")
age = 25
income = 50000
if age >= 18 and income >= 30000:
    print("Loan approved")
else:
    print("You don't qualify")

# or
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It is weekend!")
else:
    print("It's weekday!")

# not
is_raining = False
if not is_raining:
    print("Let's go for a walk!")
else:
    print("Don't go outside!")