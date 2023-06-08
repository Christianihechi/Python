# Write a program that asks the user to enter a series of numbers.
# Use a while loop to keep asking for numbers until the user enters 'quit'.
# Store these numbers in a list. After the loop ends, print the sum of all the numbers entered.

num_list = []
active = True

while active:
    num = input("Enter a series of numbers one at a time.\n"
                "All the numbers will be added together.\n"
                "Type 'quit' when you're done entering the numbers or 'repeat' to restart.\n")
    if num.lower() == 'quit':
        active = False
    else:
        try:
            num = int(num)
            num_list.append(num)
        except ValueError:
            print("Please enter a valid input.")
print("Sum of all the numbers is", sum(num_list))
