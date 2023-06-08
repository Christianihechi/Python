# Create an empty list to store the numbers
sum_list = []

# Set the loop to active
active = True

# Continue accepting numbers until the user enters 0
while active:
    num = int(input("Type a number and press Enter to enter the next number. "
                    "Type 0 when you are ready to calculate the sum.\n"))

    # Check if the number is not 0
    if num != 0:
        sum_list.append(num)
    else:
        # Calculate the sum of all the numbers entered
        total = sum(sum_list)

        # Print the sum of the numbers
        print(f"The sum of the numbers is: {total}")

        # Set the loop to inactive and exit
        active = False
