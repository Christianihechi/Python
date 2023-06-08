# Write a program that asks the user what kind of rental car they would like.
# Print a message about that car, such as Let me see if I can find you a Subaru.

car_to_rent = input('What kind of car would you like to rent?\n')
mistake = input("Did you make a typo error?\n"
                "Please type Yes, or No accordingly.\n"
                "Type 'quit' if you are not renting today.\n")
while True:
    if mistake.lower() == "quit":
        print("We are sorry to see you go.")
    break
if mistake.lower() == 'yes':
    car_correction = input("Please enter the correct car info.\n")
    print(f"Great choice! Please wait while I search for a {car_correction.title()} car.")
elif mistake.lower() == 'no':
    print(f"Great choice! Please wait while I search for a: {car_to_rent.title()} car.")
