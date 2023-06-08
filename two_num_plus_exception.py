active = True

while active:
    try:
        num1 = int(input("Enter the first number:\n"))
        num2 = int(input("Enter the second number:\n"))
        total = num1 + num2
        print("The sum is:", total)
        active = False
    except ValueError:
        print("Please enter valid integers for both numbers.")


