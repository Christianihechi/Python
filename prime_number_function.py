import math


def is_prime(number):
    # Check if number is less than 2
    if number < 2:
        return False

    # Iterate from 2 to the square root of the number
    for i in range(2, int(math.sqrt(number)) + 1):
        # Check if the number is divisible by i
        if number % i == 0:
            return False

    # If no divisors found, the number is prime
    return True


while True:
    user_input = int(input("Enter any number to check if it's a Prime number: "))
    print(is_prime(user_input))


