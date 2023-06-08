active = True

while active:
    try:
        age = int(input("Please enter your age:\n"))
        if age < 18:
            print("You are a minor.")
        elif age >= 18 and age < 65:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
        # active = False
    except ValueError:
        print("Please enter a valid input only!")
