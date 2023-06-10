# Ask the user for their choice of rental car.
car_to_rent = input('What kind of car would you like to rent?\n')

# Ask the user if they made a typo error.
mistake = input("Did you make a typo error? Please type 'Yes' or 'No' accordingly.\n")

# Check the user's response.
if mistake.lower() == "yes":
    # Prompt the user to enter the correct car information.
    car_correction = input("Please enter the correct car info.\n")
    print(f"Great choice! Please wait while I search for a {car_correction.title()}")
elif mistake.lower() == 'no':
    print(f"Great choice! Please wait while I search for a: {car_to_rent.title()}")
