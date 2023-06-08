# Get the number of people in the dinner group from the user
restaurant_seating = int(input("How many people are in your dinner group? \n"))

# Check if the dinner group exceeds the seating capacity
if restaurant_seating > 8:
    print("Sorry, please wait for the next available table!")
else:
    print("Your table is being prepared, please hold on for a call from the receptionist.")
