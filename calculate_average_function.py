import math
def calculate_average(number_list):
    """Calculate average from a list of numbers as input"""
    average = sum(number_list)/len(number_list)
    number_list = []
    print(f"The average of the given numbers is: {average}")

    return average
