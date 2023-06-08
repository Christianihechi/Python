places_to_visit = ["Abuja", "Sokoto", "Aba", "Kano", "Ibadan", "Borno"]

# Print list of places to visit
print(places_to_visit)

# Using sorted to print the list alphabetically without affecting the original list
print("Sorted list, alphabetically: ", sorted(places_to_visit))

# Confirming list is still in it's original order
print("Original list: ", places_to_visit)

# Using sorted to print the list alphabetically but reversed
print("Sorted alphabetically, but reversed: ", sorted(places_to_visit, reverse=True))

# Confirming list is still original
print("Original list check: ", places_to_visit)

# Reversing the list
places_to_visit.reverse()

# Print the reversed
print("List has been reversed: ", places_to_visit)

places_to_visit.reverse()

# Reversed again
print("Reversed yet again: ", places_to_visit)

# Using sort to change the list order
places_to_visit.sort()
print(places_to_visit)

# Using sort to change list order and also reversed
places_to_visit.sort(reverse=True)

print("Final sorting: ", places_to_visit)

# Using len() to show number of items in the list
print(f"Number of items in the list:\n{len(places_to_visit)}")
