# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

poll = {}
active = True
while active:
    name = input('What is your name?\n')
    vacation = input('Where would you like to go for vacation?\n')
    poll[name] = vacation

    repeat = input('Would you like to continue? Yes/No\n')
    if repeat.lower() == 'no':
        active = False
    elif repeat.lower() == 'yes':
        active = True
for name, vacation in poll.items():
    print(f'{name.title()} -'
          f' {vacation.title()}')
    
