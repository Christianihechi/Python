def max_of_three(num1, num2, num3):
    """Check the max of three numbers"""
    if num1 > num2 and num1 > num3:
        max_num = num1
    elif num2 > num1 and num2 > num3:
        max_num = num2
    else:
        max_num = num3
    print(f"The maximum value in {num1}, {num2}, and {num3} is: {max_num}")
    return max_num


while True:
    try:
        print("Enter three numbers to check the maximum\n")
        num_1 = float(input("Enter 1st number: "))
        num_2 = float(input("Enter the 2nd number: "))
        num_3 = float(input("Enter the 3rd number: "))
        print()
        large = (max_of_three(num_1, num_2, num_3))
        break

    except ValueError:
        print("Please enter only integers or floats, not some weird stuffs!")
