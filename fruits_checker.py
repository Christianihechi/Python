# Create a list of fruits.
fruits = ['mango', 'watermelon', 'pineapple', 'pear', 'lemon', 'cashew', 'orange',
          'grape', 'guava', 'pawpaw', 'lime', 'coconut', 'sugarcane', 'pepper',
          'okra', 'potato', 'yam', 'casava', 'kola', 'groundnut', 'maize', 'corn']

# Set the initial value for the loop control variable.
active = True

# Start a while loop to repeatedly ask the user for their favorite fruit.
while active:
    # Ask the user to enter their favorite fruit or 'quit' to exit.
    user_input = input("What is your favorite fruit?\nTo stop, type 'quit'\n")

    # Check if the user's input exists in the list of fruits.
    if user_input.lower() in fruits:
        print(f"Great choice! {user_input} is available and is very healthy!")
        active = False
    # Check if the user wants to quit.
    elif user_input.lower() == 'quit':
        active = False
    # If the input is not a valid fruit or 'quit', ask the user to try again.
    else:
        print("Try again!")

