# Write a program that asks the user to enter a number.
# Use a while loop to keep asking for a number until the user enters a valid integer.
# Once a valid number is entered, print a message displaying the square of that number.

active = True
while active:
    user_input = input("Enter a number to check it's square:\n")
    if not user_input.isdigit():
        print("Please enter a valid integer.\n")
    else:
        user_input = int(user_input)
        print(f"Square of {user_input} is :\n {user_input ** 2}")

# Using the Try and Catch procedure.

active = True
while active:
    try:
        user_input = input("Enter a number to check its square:\n")
        user_input = float(user_input)
        print("The square is ", (user_input ** 2))
        active = False
    except ValueError:
        print("It seems you entered an invalid input. Numbers only !")
