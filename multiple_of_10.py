# Ask the user to enter a number. Input is set to an integer
number = int(input('Please enter a number:\n'))

# Check if the number is a multiple of 10.
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
