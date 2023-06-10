# Set the initial value for the loop control variable.
active = True

# Start an infinite loop.
while active:
    try:
        # Ask the user to input their age.
        age = int(input("Please enter your age:\n"))

        # Check the age and print the corresponding message.
        if age < 18:
            print("You are a minor.")
        elif age >= 18 and age < 65:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")

        # active = False

    # Handle the ValueError exception if the user enters an invalid input.
    except ValueError:
        print("Please enter a valid input only!")
