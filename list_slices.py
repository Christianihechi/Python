# list_of_gays = ["El Patron", "Overcomer", "Conrado", "Peluche", "Gold Boo"]
#
# # Let's see the number of items in the list
# print(f"The number of gays in Mehico are:\n {len(list_of_gays)}")
# print("The first three gays are: \n")
# gays_3 = (list_of_gays[:3])
# for i in gays_3:
#     print(i)
#
# list_of_gays.append("Chidi")
# print(f"Newly updated gay list: ", sorted(list_of_gays))


favourite_food = ["pizza", "falafel", "carrot cake", "cannoli", "ice cream"]
print("The first three items in the list are::")
for foods in favourite_food[:3]:
 print(foods.title())

print("Three items from the middle of the list are:\n")
for foods in favourite_food[1:4]:
 print(foods.title())

print("The last three items in the list are:\n")
best_food = favourite_food[:]
for food in best_food[-3:]:
 print(food.title())

# Copying list and slices exercise
my_fave_food = ["Onugbu", "Semo", "Rice", "Ofe Nsala", "Plantain Porridge", "Spagheti"]

# Copying from my_fave_food to my_friends_fave
my_friends_fave = my_fave_food[:]

# Adding a new food to the original list and also to the new list
my_fave_food.append("Custard")
my_friends_fave.append("Tea and Bread")

# Printing the items in the original
print("My favorite food includes: \n")
for food in my_fave_food:
 print(food)

# Printing the items in the copied list
print("My friend's favorite food includes: \n")
for food in my_friends_fave:
 print(food)