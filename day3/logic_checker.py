# combines logical, identity, and membership operations
list_checker = ["apple", "banana", "orange"]
fruits = ["mango", "cherry", "apple"]

print("apple" in list_checker and "apple" in fruits)    # True
print(list_checker is not fruits)                       # True
print("pineapple" in fruits)                            # False
