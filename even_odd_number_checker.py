# Check if a number is even or odd using the Modulo operator %

number = input("Enter a number, and I'll tell you if it's even or odd:\n ")
number = int(number)
if number % 2 == 0:
 print(f"\nThe number {number} is even.")
else:
 print(f"\nThe number {number} is odd.")
