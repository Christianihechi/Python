# Prompt the user to enter a name or 'quit' to stop.
prompt = "\nType any name and I will say Hi to the person."
prompt += "\nTo stop, type 'quit'.\n"

# Initialize an empty message variable.
message = ""

# Set the initial value for the loop control variable.
active = True

# Start a while loop to repeatedly get input from the user.
while active:
    # Ask the user to enter a name.
    message = input(prompt)

    # Check if the user wants to quit.
    if message.lower() != 'quit':
        print(f"Hi, {message}")
    else:
        active = False
