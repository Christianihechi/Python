# Print a message from the user

prompt = "\nType any name and I will say Hi to the person."
prompt += "\nTo stop, type 'quit'.\n"

message = ""
active = True
while active:
    message = input(prompt)
    if message.lower() != 'quit':
        print(f"Hi, {message}")
    else:
        active = False
