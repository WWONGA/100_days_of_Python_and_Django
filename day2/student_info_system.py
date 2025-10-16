# Student Information System:

# Real world Project: A Simple Student Information System
student_name = input("Enter student's name: ")
student_surname = input("Enter student's surname: ")
student_age = int(input("Enter student's age: "))
student_grade = input("Enter student's grade: ")
favourite_subject = input("Enter favourite subject: ")
has_passed = input("Has the student passed? (yes / no): ")

print("\n---Student Report ---")
print(f"Name: {student_name} {student_surname}")
print(f"Age: {student_age}")
print(f"Grade: {student_grade}")
print(f"Favourite Subject: {favourite_subject}")
print(f"Passed: {has_passed.lower()}")
print(f"----------------------")
