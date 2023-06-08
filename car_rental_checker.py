# Ask the user for their choice of rental car.
car_to_rent = input('What kind of car would you like to rent?\n')

# Ask the user if they made a typo error or if they want to quit.
mistake = input("Did you make a typo error?\n"
                "Please type 'Yes' or 'No' accordingly.\n"
                "Type 'quit' if you are not renting today.\n")

# Start an infinite loop to handle user input.
while True:
    # Check if the user wants to quit.
    if mistake.lower() == "quit":
        print("We are sorry to see you go.")
        break

    # Check if the user made a typo error.
    if mistake.lower() == 'yes':
        # Prompt the user to enter the correct car information.
        car_correction = input("Please enter the correct car info.\n")
        print(f"Great choice! Please wait while I search for a {car_correction.title()} car.")
    elif mistake.lower() == 'no':
        print(f"Great choice! Please wait while I search for a: {car_to_rent.title()} car.")
        
    # Exit the loop after processing the input.
    break
