# Create a dictionary called 'countries' with country names as keys and their capitals as values.
countries = {
    'Nigeria': 'Abuja',
    'Afghanistan': 'Kabul',
    'United States Of America': 'Washington D.C.',
    'Algeria': 'Algiers',
    'Angola': 'Luanda',
    'Argentina': 'Buenos Aires'
}

# Set the flag 'active' to True to control the while loop.
active = True

# Start the while loop to keep asking for a country's name until a valid country is entered.
while active:
    # Ask the user to enter a country's name and convert it to title case.
    user_input = input("Enter any country's name:\n").title()

    # Check if the user_input exists as a key in the 'countries' dictionary.
    if user_input in countries.keys():
        # Retrieve the capital corresponding to the entered country.
        capital = countries[user_input]
        # Print the capital of the entered country.
        print(f"The capital of {user_input} is {capital}.")
        # Set 'active' to False to exit the while loop.
        active = False
    else:
        # If the entered country is not found in the dictionary, display an error message.
        print("Please enter a valid country. Make sure you type the name in full.")
