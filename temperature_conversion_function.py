def celsius_to_fahrenheit(c):
    """Convert temperature from Celsius to Fahrenheit"""
    f = (c * 1.8) + 32
    print(f"{c} degrees Celsius to Fahrenheit is: {f} degrees Fahrenheit.")
    return f


def fahrenheit_to_celsius(f):
    """Convert temperature from Fahrenheit to Celsius"""
    c = (f - 32) / 1.8
    print(f"{f} degrees Fahrenheit to Celsius is: {c} degrees Celsius.")
    return c


active = True
while active:
    user_input = input("For Celsius to Fahrenheit, enter 'c'\n"
                       "For Fahrenheit to Celsius, enter 'f'.\nEnter 'q' to exit.\n")
    if user_input.lower() == 'c':
        cel = float(input("Enter Celsius value: "))
        celsius_to_fahrenheit(cel)

    elif user_input.lower() == 'f':
        fah = float(input("Enter Fahrenheit value: "))
        fahrenheit_to_celsius(fah)

    elif user_input.lower() == 'q':
        active = False

    else:
        print("Please enter a valid input.\n")
