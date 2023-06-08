# Ask a user for their kind of rental car

car_to_rent = input('What kind of car would you like to rent?\n')
mistake = input("Did you make a typo error? Please type Yes, or No accordingly.\n")
if mistake.lower() == "yes":
    car_correction = input("Please enter the correct car info.\n")
    print(f"Great choice! Please wait while I search for a {car_correction.title()}")
elif mistake.lower() == 'no':
    print(f"Great choice! Please wait while I search for a: {car_to_rent.title()}")
