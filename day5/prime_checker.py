# Prime numbers:
number = int(input("Enter a Number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number.")
            break
    else:
        print(number, "is a prime number.")
else:
    print("Enter a number GREATER THAN 1.")