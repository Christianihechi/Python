# Create a program that conducts a poll by asking users to answer a question.
# Store the responses in a dictionary where each user's name is the key and their response is the value.
# Allow users to quit the poll by entering a specific value, such as 'quit'
# Finally, display the poll results by printing each user's name and their response.

polls = {}
active = True

while active:
    name = input("What is your name? Enter your name or 'quit' to close the poll.\n")

    if name.lower() == 'quit':
        active = False
        print("Goodbye!")
    else:
        response = input("What is your favourite sports game?\n")
        if response.lower() == 'quit':
            active = False
            print("Goodbye!")
        else:
            polls[name] = response
print("\n--- Poll Results ---")

for user, sports in polls.items():
    print(f"Name: {user.title()}\nFavourite Sports: {sports.title()}")
