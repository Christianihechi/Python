# Make a Poll for collection of names and favourite cities.

# Create an empty dictionary to store the user's inputs
responses = {}
polling_active = True

while polling_active:
    name = input("What is your name\n")
    city = input("What is your favourite city in Nigeria?\n")
    responses[name] = city

    repeat = input("Would you like to take another poll? Yes/No\n")
    if repeat.lower() == 'no':
        polling_active = False
    elif repeat.lower() == 'yes':
        polling_active = True
for name, city in responses.items():
    print(f"{name.title()} would love to visit {city.title()} in Nigeria.\n")
    
