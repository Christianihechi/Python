# Create an empty dictionary to store the poll responses.
poll = {}

# Set the initial value for the loop control variable.
active = True

# Start a while loop to conduct the poll.
while active:
    # Ask the user for their name.
    name = input("What is your name?\n")

    # Ask the user where they would like to go for vacation.
    vacation = input("If you could visit one place in the world, where would you go?\n")

    # Store the user's response in the dictionary.
    poll[name] = vacation

    # Ask if the user wants to continue the poll.
    repeat = input("Would you like to continue? Yes/No\n")

    # Check if the user wants to continue or quit.
    if repeat.lower() == 'no':
        active = False
    elif repeat.lower() == 'yes':
        active = True

# Print the poll results by iterating over the dictionary.
for name, vacation in poll.items():
    print(f"{name.title()} - {vacation.title()}")
