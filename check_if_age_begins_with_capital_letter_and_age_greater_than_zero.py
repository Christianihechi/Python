active = True

while active:
    # Prompt the user to enter their name
    name = input("What is your name?\n")

    # Prompt the user to enter their age and convert it to an integer
    age = int(input("What is your age?\n"))

    # Check if the name starts with a capital letter and age is greater than 0
    if name == name.title() and age > 0:
        # If the inputs are valid, print a personalized message
        print(f"Hello {name}, your age is {age}. You are eligible for the club membership!")
        active = False  # Exit the while loop
    else:
        # If the inputs are invalid, display an error message
        print("Please start your name with uppercase and your age must be above 0.")
