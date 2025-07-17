# Nested conditionals
age = 17
has_permission = True

if age >= 18:
    print("You can vote.")
else:
    if has_permission:
        print("You can vote with supervision.")
    else:
        print("Sorry. You are not allowed to vote.")