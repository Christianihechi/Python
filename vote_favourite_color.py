# Create an empty dictionary
polls = {}
# set a variable to True
active = True

# Start a while loop that will prompt the user to enter their favourite color.

while active:
    color = input("What is your favourite color? Type 'quit' to exit\n")
    if color.lower() == 'quit':
        active = False
    else:
        if color in polls:
            polls[color] += 1
        else:
            polls[color] = 1
print("\n--- Poll Results ---")
for color, count in polls.items():
    print(f"{color.title()}: {count} votes")
