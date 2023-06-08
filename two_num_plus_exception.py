# Set the loop to active
active = True

# Continue the loop until valid integers are entered
while active:
    try:
        # Prompt the user to enter the first number and convert it to an integer
        num1 = int(input("Enter the first number:\n"))

        # Prompt the user to enter the second number and convert it to an integer
        num2 = int(input("Enter the second number:\n"))

        # Calculate the sum of the two numbers
        total = num1 + num2

        # Print the sum
        print("The sum is:", total)

        # Set active to False to exit the loop
        active = False

    except ValueError:
        # Handle the exception if the user enters invalid input
        print("Please enter valid integers for both numbers.")
