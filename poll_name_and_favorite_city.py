# Create an empty dictionary to store the user's inputs.
responses = {}

# Set the initial value for the loop control variable.
polling_active = True

# Start a while loop to conduct the poll.
while polling_active:
    # Ask the user for their name.
    name = input("What is your name?\n")

    # Ask the user for their favorite city in Nigeria.
    city = input("What is your favorite city in Nigeria?\n")

    # Store the user's response in the dictionary.
    responses[name] = city

    # Ask if the user wants to take another poll.
    repeat = input("Would you like to take another poll? Yes/No\n")

    # Check if the user wants to continue or quit.
    if repeat.lower() == 'no':
        polling_active = False
    elif repeat.lower() == 'yes':
        polling_active = True

