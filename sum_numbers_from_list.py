# Write a program that asks the user to enter a series of numbers.
# Use a while loop to keep accepting input until the user enters a specific value, such as 0.
# Then, calculate and display the sum of all the numbers entered.

sum_list = []
active = True

while active:
    num = int(input("Type a number and press Enter to allow you type the next number. "
                    "Type 0 when you are ready to add all the numbers.\n"))
    if num != 0:
        sum_list.append(num)
    else:
        total = sum(sum_list)
        print(f"The SUM of the numbers is:\n{total}")
        active = False
