# cars = ["Toyota", "range rover", "camry", "limousine", "bently"]
#
# for car in cars:
#     if car == "toyota":
#         car.lower() == "toyota"
#         print(car.upper())
#     else:
#         print(car.title())
import math

# Conditional tests include if, or, not, True, False,

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
#
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
#
# winning_number = 35
# print("\nIs Winning Number == '40'? I predict False. ")
# print(winning_number == 40)
#
# winning_number = 35
# print("\nIs Winning Number == '35'? I predict True. ")
# print(winning_number == 35)
#
# no_of_boys = 355
# print("\nNumber of boys is '355', I predict True.")
# print(no_of_boys == 355)
#
# no_of_boys = 355
# print("\nNumber of boys is '366', I predict False.")
# print(no_of_boys == 366)

# Tests for equality and inequality with strings

# cars = ('Benz', 'Spider', 'Rolls Royse', 'Avantis')
# for car in cars:
#     if car == 'rolls royse':
#         print(car.upper())
#     else:
#         print(car.title())

# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

# people_and_age = []
# for i in range(5):
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     people_and_age.append({"name":name, "age":age})
#
# for person in people_and_age:
#     if person['age'] >= 18:
#         print ("Hello,",name.title(), "you're an adult because you are", age, "years old.")
#     else:
#         print("None of you is up to mthe age of getting married, keep building yourselves !")

# people = []
# for i in range(5):
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     people.append({'name': name, 'age': age})
#
# for person in people:
#     if person['age'] > 18:
#         print(person['name'], "is an adult.")
#     else:
#         print(person['name'], "is a minor.")

# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

# breads = ['Butter bread', 'Fruit bread', 'Milk bread', 'Butter cake']
# if 'Butter cake' not in breads:
#     print("We do not have Butter cake")
# else:
#     print("It's available. Anything else?.")


# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $25.
# Admission for anyone age 18 or older is $40.

# age = int ( input ( "How old are you?\n" ) )
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40
# print(f"Your admission cost is ${price}.")

# Aliens colors and points

# alien_color = input('What is the color of the alien?\n')
# if alien_color == 'Green' or 'green':
#     print("You just earned 5 points!")
# elif alien_color == 'Red' or 'red':
#     print("You just earned 15 points!")
# elif alien_color == 'Yellow' or 'yellow':
#     print("You just earned 10 points!")

# Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:

# age = int(input("What is your age?\n"))
# if age <2:
#     print("You are a baby.")
# elif age == 2 or age <4:
#     print("You are a toddler.")
# elif age == 4 or age < 13:
#     print("You are a kid.")
# elif age == 13 or age < 20:
#     print("You are a teenager")
# elif age == 20 or age < 65:
#     print("You are an adult.")
# else:
#     print("You are an elder.")

# Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.

# Username

# create a list
# persons = ['admin', 'john', 'emeka', 'lilian', 'ada']
# if persons:
#     for person in persons:
#         if person == 'admin':
#             print('Hello admin, would you like to see a status report?')
#         else:
#             print(f'Hello {person.title()}, thank you for logging in again.')
# else:
#     print('We need to find some users!')

# Checking Usernames
# current_users = ['philip', 'mercy', 'chidimma', 'precious', 'anioke', 'ikenna']
# new_users = ['philip', 'ebere', 'mercy', 'chidimma', 'precious', 'anioke']
#
# current_user_lower = [user.lower() for user  in current_users]
#
# for user in new_users:
#     if user in current_users:
#         print(f"{user} is taken. Please enter a new username!")
#     else:
#         print(f'"{user}" username is available')

#  Ordinal Numbers
# ordinal_numbers = [1,2,3,4,5,6,7,8,9]
# for number in ordinal_numbers:
#     if number == 1:
#         print("1st\n")
#     elif number == 2:
#         print("2nd\n")
#     elif number == 3:
#         print("3rd\n")
#     else:
#         print(f"{number}th\n")

# Using Python to calculate the lenght of a smartphone  using its width, height, and thickness
# import math
# width = float(input("What is the width?\n"))
# height = float(input("What is the height?\n"))
# thickness = float(input("What is the thickness?\n"))
# # Length = square root of (Width squared + Height squared + Thickness squared)
# lenght = math.sqrt(width ** 2 + height ** 2 + thickness ** 2)
# print(lenght)
# inches = (lenght * 0.03937)
# print("Inches = ", inches, "inches")

