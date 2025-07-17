understood_topic = True
is_distracted = False

name = input("What is your name? ")
hours = int(input("You studied for how many hours today? "))        # String input into int value
if hours >= 4 and understood_topic and not is_distracted:
    print("✅ You did Great Job!", name)
else:
    print("❗Try to focus tomorrow.", name)