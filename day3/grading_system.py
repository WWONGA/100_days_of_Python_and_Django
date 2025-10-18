# Mini Project
# Ask the user to enter marks for three subjects.

"""
Calculate the average using arithmetic operators.
Use comparison operators to assign grades:
80–100 → A
70–79 → B
60–69 → C
50–59 → D
Below 50 → Fail
"""

"""
Print results like this:

--- Student Grade Report ---
Average: 76.7
Grade: B
Status: Pass
"""

maths = float(input("Enter Maths results: "))
physics = float(input("Enter Physics results: "))
chemistry = float(input("Enter Chemistry results: "))
average = (maths + physics + chemistry) / 3
print(" --- Student Grade Report --- ")
print(f"Average: {average: .2f}")
if average >= 80 and average <= 100:
    print("Grade: A")
    print("Status: Pass")
elif average >= 70 and average < 80:
    print("Grade: B")
    print("Status: Pass")
elif average >= 60 and average < 70:
    print("Grade: C")
    print("Status: Pass")
elif average >= 50 and average < 60:
    print("Grade: D")
    print("Status: Pass")
else:
    print("Fail")