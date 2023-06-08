# Ask the user for their age.
age = input("How old are you? ")

# Convert the age to an integer.
age = int(age)

# Check if the age is 18 or higher.
if age >= 18:
    print("You can proceed!")
else:
    print("You're not eligible!")
