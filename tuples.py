# # Defining a Tuple. Note, unlike Lists, Tuples are immutable.
# monthly_pay = (str("N200 Naira"), str("N500 Naira"), str("N1000 Naira"))
# print(monthly_pay[0])
# print(monthly_pay[1])
# print(monthly_pay[2])
#
# print("\n")
#
# for pay in monthly_pay:
#     print(pay)
#
# my_t = (3,4,4,str("God"))
# print(type(my_t))
# print(type(monthly_pay))


# # Five foods in a buffet!
# buffet_food = ("Rice", "Beans and Yam", "Spag", "Egusi soup and Fufu", "Yam and Egg Sauce")
# for food in buffet_food:
#     print (food)

# Five foods in a buffet!
buffet_food = ("Rice", "Beans and Yam", "Spag", "Egusi soup and Fufu", "Yam and Egg Sauce")
for food in buffet_food:
    print(food)
print("Total items:\n",len(buffet_food))


# Let's print just the first 3 foods
my_new_food = buffet_food[:]
for i in range(3):
    print(my_new_food[i])

