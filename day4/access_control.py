# Permission App
age = int(input("Enter your age: "))
has_id = input("Do you have an ID (yes or no): ").lower()

if age >= 18:
    if has_id == "yes":
        print("Access Granted!")
    else:
        print("You can't enter without showing an ID")
else:
    print("You are too young, ACCESS DENIED!")