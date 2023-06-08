# Create an empty list to store the numbers
num_list = []

# Set the loop to active
active = True

# Continue asking for numbers until the user enters 'quit'
while active:
    num = input("Enter a series of numbers one at a time.\n"
                "All the numbers will be added together.\n"
                "Type 'quit' when you're done entering the numbers or 'repeat' to restart.\n")

    # Check if the user entered 'quit'
    if num.lower() == 'quit':
        active = False
    else:
        try:
            # Convert the input to an integer and append it to the list
            num = int(num)
            num_list.append(num)
        except ValueError:
            print("Please enter a valid input.")

# Calculate the sum of all the numbers in the list
total = sum(num_list)

# Print the sum of the numbers
print("Sum of all the numbers is", total)
