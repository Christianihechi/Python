states = ["Kogi", "Abuja", "Adamawa", "Yola", "Benue", "Enugu", "Markudi", "Jos", "Osun", "Rivers", "Lagos", "Kano", "Benin", "Delta", "Plateau"]

# Print the list of some of the states in Nigeria
print("Some of the states in Nigeria: ", states)

# let's print the list in a sorted way without modifying the actual list
print("States in alphabetical order: ", sorted(states))

# Check if the original order is still valid
print("States in original order: ", states)

# Let's sort the list again but in reversed aphabetical order without altering the original list
print("States in reversed alphabetical order: ", sorted(states, reverse=True))

# let's now print the original list to check if it's still untouched
print("Original list check:", states)

# Let's reverse the list
states.reverse()

# Print the reversed order
print("States reversed", states)

# Let's reverse the list again to the former pattern
states.reverse()

# Print the reversed order
print("States reversed", states)

# Let's permanently sort the list in alpahbetical order
states.sort()

# Printing the sorted list
print("List has been sorted: ", states)

# Sorting in reversed order and saving it to the original value
states.sort(reverse=True)

print("List has been sorted but reversed: ", states)

# let's check the number of the items in the list
print("Number of total states in  the list: ", len(states))