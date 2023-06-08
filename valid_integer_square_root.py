        active = True
while active:
    try:
        # Prompt the user to enter a number
        user_input = input("Enter a number to check its square:\n")
        
        # Attempt to convert the user input to an integer
        user_input = int(user_input)
        
        # Calculate the square of the number
        square = user_input ** 2
        
        # Print the result
        print(f"The square of {user_input} is: {square}")
        
        # Set active to False to exit the loop
        active = False
    except ValueError:
        # If a ValueError is raised, the input is not a valid integer
        # Display an error message and continue the loop to prompt for a valid input
        print("Please enter a valid integer.\n")
