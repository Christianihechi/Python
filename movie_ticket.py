# A movie theater charges different ticket prices depending on a person’s age.
# If a person is under the age of 3, the ticket is free
# If they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prompt = "Enter your age to check your movie ticket cost"
prompt += "Type 'quit' and press Enter to exit.\n"

while True:
    age_checker = input(prompt)
    if age_checker.lower() == 'quit':
        break
    age = int(age_checker)
    if age <= 3:
        print("Your ticket fee is $0")
    elif 3 < age <= 12:
        print("Your ticket fee is $10")
    else:
        print("Your ticket fee is $15")
