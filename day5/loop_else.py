# Else on for loop
for i in range(5):
    print(i)
else:
    print("Loop completed successfully!")

# Using break, else won't run:
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print because loop was broken.")


