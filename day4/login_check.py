# Login logic
username = "admin"
password = 1234
entered_username = input("What is your Username? ").lower()
entered_password = int(input("What is your Password: "))

if entered_username == username:
    if entered_password == password:
        print("Successfully logged in")
    else:
        print("Wrong password!")
else:
    print("Username not found")