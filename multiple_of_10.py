# Check if user input is a multiple of 10

number = int(input('Please enter a number: \n'))
if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f'{number} is not a multiple of 10.')
