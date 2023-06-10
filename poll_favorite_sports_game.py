# Initialize an empty dictionary to store the poll responses.
polls = {}

# Set the initial value for the loop control variable.
active = True

# Start a while loop to conduct the poll.
while active:
    # Ask the user for their name or 'quit' to close the poll.
    name = input("What is your name? Enter your name or 'quit' to close the poll.\n")

    # Check if the user wants to quit.
    if name.lower() == 'quit':
        active = False
        print("Goodbye!")
    else:
        # Ask the user for their favorite sports game.
        response = input("What is your favorite sports game?\n")

        # Check if the user wants to quit.
        if response.lower() == 'quit':
            active = False
            print("Goodbye!")
        else:
            # Store the user's response in the dictionary.
            polls[name] = response

print("\n--- Poll Results ---")

# Print the poll results by iterating over the dictionary.
for user, sports in polls.items():
    print(f"Name: {user.title()}\nFavorite Sports: {sports.title()}")
