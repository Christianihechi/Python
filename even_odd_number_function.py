def even_number_checker(check_number):
    """Check if a number is even or odd"""
    try:
        check_number = int(check_number)
        if check_number % 2 == 0:
            print(f"{check_number} is an Even number.\n")
        elif check_number % 2 != 0:
            print(f"{check_number} is an Odd number.")
    except ValueError:
        print("Please enter integers only! Try again.")


while True:
    user_input = input("\nPlease enter any number to check if it's Even or Odd: ")
    even_number_checker(user_input)
