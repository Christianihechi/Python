# Write a program that generates a random number between 1 and 10.
# The user should guess the number, and the program should provide feedback if the guess is too high or too low.
# The program should continue to prompt the user for guesses
# Until they correctly guess the number. 

import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Start a while loop to prompt the user for guesses
while True:
    # Get the user's guess
    guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess is correct
    if guess == random_number:
        break

    # Check if the guess is too low or too high
    if guess > random_number:
        print("The number is lower than that. Please guess again.")
    elif guess < random_number:
        print("The number is higher than that. Please guess again.")
