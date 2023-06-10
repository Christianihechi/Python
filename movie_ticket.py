# Prompt for user input and provide instructions.
prompt = "Enter your age to check your movie ticket cost. "
prompt += "Type 'quit' and press Enter to exit.\n"

# Start an infinite loop to continuously ask for user input.
while True:
    # Ask the user for their age or 'quit' to exit.
    age_checker = input(prompt)

    # Check if the user wants to exit the loop.
    if age_checker.lower() == 'quit':
        break

    # Convert the input to an integer for comparison.
    age = int(age_checker)

    # Determine the ticket cost based on the age provided and print the result.
    if age <= 3:
        print("Your ticket fee is $0")
    elif 3 < age <= 12:
        print("Your ticket fee is $10")
    else:
        print("Your ticket fee is $15")
