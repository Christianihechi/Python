# Write a program that asks users to enter their favorite programming language.
# Allow them to enter as many languages as they want.
# When they're done, display the total number of votes for each language.

votes = {}
active = True

while active:
    language = input("Enter your favorite programming language (or 'quit' to exit): ")
    if language.lower() == 'quit':
        active = False
    else:
        if language in votes:
            votes[language] += 1
        else:
            votes[language] = 1

print("\n--- Poll Results ---")
for language, count in votes.items():
    print(f"{language.title()}: {count} votes")

