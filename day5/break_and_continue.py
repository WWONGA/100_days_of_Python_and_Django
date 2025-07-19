# Break (for loop):
for i in range(1, 10):
    if i == 5:
        break   # when i is 5, stop and 5 is not printed
    print(i)

# Continue (for loop):
for i in range(1, 10):
    if i == 5:
        continue    # print from 1 to 9 (but jump/skip 5)
    print(i)