# Guess a number:

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number from (1 - 10): "))

    if guess < 7:
        print("Too low!")
    elif guess > 7:
        print("Too high")
    else:
        print(f"Correct: {guess} is the secret number!")