def reverse_string(user_input):
    """Reverses any string"""
    reversed_string = ""
    for char in user_input[::-1]:
        reversed_string += char
    return reversed_string


while True:
    prompt = input("What would you like view in reversed order?\nPlease enter 'q' to exit.\n")
    if prompt.lower() == 'q':
        break
    else:
        reverse = reverse_string(prompt)
        print(f"The reverse of {prompt} is:\n{reverse}\n")
