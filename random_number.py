# Write a program that generates a random number between 1 and 100.
# The user should guess the number, and the program should provide feedback if the guess is too high or too low.
# The program should continue to prompt the user for guesses
# Until they correctly guess the number. Use the following three approaches:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user guesses the correct number.

import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

while True:
    # Get the user's guess
    guess = int(input())

    # Check if the guess is correct
    if guess == random_number:
        break

    # Check if the guess is too low or too high
    if guess >= random_number:
        print("The number is lower than that. Please guess again.")
    elif guess <= random_number:
        print("The number is higher than that. Please guess again.")
        
