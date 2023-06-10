# Prompt the user to enter pizza toppings or 'quit' to stop.
prompt = "Please type the pizza toppings you want and press 'Enter'."
prompt += "\nType 'quit' and press 'Enter' when you're done.\n"

# Initialize an empty string for toppings.
toppings = ""

# Start a while loop to repeatedly ask for pizza toppings.
while True:
    # Ask the user to enter a topping.
    toppings = input(prompt)

    # Check if the user wants to quit.
    if toppings.lower() != 'quit':
        print(f"{toppings.title()} is being added to your pizza.")
    else:
        break
