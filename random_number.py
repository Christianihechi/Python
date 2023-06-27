import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Start a while loop to prompt the user for guesses
while True:
    try:
        # Get the user's guess
        guess = int(input("Guess a number between 1 and 10: "))

        # Check if the guess is correct
        if guess == random_number:
            print(f"Your guess, {guess} is correct!")
            break

        # Check if the guess is too low or too high
        if guess > random_number:
            print("The number is lower than that. Please guess again.")
        elif guess < random_number:
            print("The number is higher than that. Please guess again.")
    except ValueError:
        print("That's probably not a number !")
