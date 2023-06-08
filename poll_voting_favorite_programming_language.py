# Create an empty dictionary to store the votes for each programming language.
votes = {}

# Set the initial value for the loop control variable.
active = True

# Start a while loop to collect the votes.
while active:
    # Ask the user to enter their favorite programming language.
    language = input("Enter your favorite programming language (or 'quit' to exit): ")

    # Check if the user wants to quit.
    if language.lower() == 'quit':
        active = False
    else:
        # Add the vote to the dictionary.
        if language in votes:
            votes[language] += 1
        else:
            votes[language] = 1

print("\n--- Poll Results ---")

# Print the poll results by iterating over the dictionary.
for language, count in votes.items():
    print(f"{language.title()}: {count} votes")
