# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza

prompt = "Please type the Pizza toppings you want and press 'Enter'"
prompt += "\nType 'quit' and press 'Enter' when you're done.\n"

toppings = ""
while True:
    toppings = input(prompt)
    if toppings.lower() != 'quit':
        print(f"{toppings.title()} is being added to your Pizza")
    else:
        break
