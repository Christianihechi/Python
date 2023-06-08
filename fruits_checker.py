# Create a list of fruits and ask the user to enter the name of a fruit.
# Use a While loop to check if the entered fruit exists in the list.
# If it does, print a message saying it's a healthy choice.
# If it doesn't, ask the user to try again.
# Repeat this process until the user enters a valid fruit or enters 'quit' to exit.

fruits = ['mango', 'watermelon', 'pineapple', 'pear', 'lemon', 'cashew', 'orange',
          'grape', 'guava', 'pawpaw', 'lime', 'coconut', 'sugarcane', 'pepper',
          'okra', 'potato', 'yam', 'casava', 'kola', 'groundnut', 'maize', 'corn' ]

active = True
while active:
    user_input = input("What is your favourite fruit?\n"
                       "To stop, type 'quit'\n")
    if user_input.lower() in fruits:
        print(f"Great choice! {user_input} is a available and is very healthy!")
        active = False
    elif user_input.lower() == 'quit':
        active = False
    else:
        print("Try again !")
