# Create an empty dictionary to store the poll results
polls = {}

# Set a variable to True to control the loop
active = True

# Start a while loop that will prompt the user to enter their favorite color
while active:
    color = input("What is your favorite color? Type 'quit' to exit\n")
    
    # If the user enters 'quit', set active to False to exit the loop
    if color.lower() == 'quit':
        active = False
    else:
        # If the color is already in the dictionary, increment its count by 1
        if color in polls:
            polls[color] += 1
        else:
            # If the color is not in the dictionary, add it with a count of 1
            polls[color] = 1

# Print the poll results
print("\n--- Poll Results ---")
for color, count in polls.items():
    print(f"{color.title()}: {count} votes")
