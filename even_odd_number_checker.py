# Ask the user for a number.
number = input("Enter a number, and I'll tell you if it's even or odd:\n")

# Convert the input to an integer.
number = int(number)

# Check if the number is even or odd using the modulo operator (%).
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
