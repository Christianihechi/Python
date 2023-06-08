# Info on a person

# data = {
#     'name': 'Sydal Manhatan',
#     'city': 'Manhatan',
#     'phone': 23475674,
#     'age': 15
# }
#
# print(data['city'])
# print(data['age'])
# print(data['name'])
# print(data['phone'])

# saving favourite numbers and names

# fave_numbers {}
#
# for i in range(5):
#     name = input("What is your name?\n")
#     number = int(input("What is your favourite number?\n"))
#     'name' = name
#     number = number
#     fave_numbers.append

# Favourite numbers

# fave_nums = {'Ada': 13, 'Olisa': 23, 'Mark': 25, 'Ezekiel': 15}
#
# print(f"Ezekiel's favourite number is {fave_nums['Ezekiel']}" )
# print(f"Mark's favourite number is {fave_nums['Mark']}" )
#
# persona_data = {}
#
# for i in range(5):
#     name = input("Enter a name: ")
#     age = input("Enter their age: ")
#     persona_data[name] = age
#
# print(persona_data)


# Dictionary

# glossary = {'List': 'A list is a mutable datatype in Python that can store data, allow access to the data and methods as well.',
#             'Tuple': 'Unlike list, the only difference between a Tuple is that a Tuple does not allow changes to the data in it.',
#             'String': 'A string is a data type that stores letters, characters, numbers etc',
#             'Integer': 'An integer is a datatype that allows storing of numerical data like 1 2 3 4 5 6 7 8 9 10, etc. ',
#         }
#
# del glossary['Integer']
#
# print(f"\nTuple:\n{glossary['Tuple']}")
# print(f"\nList:\n{glossary['List']}")
# print(f"\nString:\n{glossary['String']}")
#
# point_value = glossary.get('Integer')
# print(point_value)

# Dictionary storing the apartments in Patemax and the price

# apartments = {
#     'room_101': 'N155,000',
#     'room_102': 'N200,000',
#     'room_103': 'N250,000',
#     'room_104': 'N300,000',
# }
#
# # for room, price in apartments.items():
# #     print(f"\nFor:{room.title()}:\nPrice:{price}")
#
# for room, price in apartments.items():
#     print(f"\nFor:{room.title()}\nPrice:{price}")


# bio_data = {
#     'chukwuma': 23,
#     'anita': 25,
#     'agatha': 32,
#     'sommy': 28,
# }
#
# for names in sorted(bio_data.keys()):
#     print(f"Names: {names.title()}")

# Exercises

# fave_num = {}
#
# for i in range(4):
#     name = input("What is your name?")
#     num = int(input("What is your favorite number?"))
#     bio_data[name] = num
# print(bio_data)


# Dictionary storing the apartments in Patemax and the price

# apartments = {
#     'room_101': 'N155,000',
#     'room_102': 'N200,000',
#     'room_103': 'N250,000',
#     'room_104': 'N300,000',
# }
# print ( f"\nWe have just four rooms available today at the following prices per night." )
#
# for room in apartments.items():
#     print(f"ROOM 101\nPrice:{apartments['room_101']}")
#     print ( f"ROOM 102\nPrice:{apartments [ 'room_102' ]}" )


#  Make a dictionary containing three major rivers and the country
#  Each river runs through.
#  Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#  Use a loop to print the name of each river included in the dictionary.
#  Use a loop to print the name of each country included in the dictionary.


# rivers_and_countries = {
#     'the nile': 'egypt',
#     'the amazon': 'brazil',
#     'the yangtze': 'china',
#     'the mississipi river': 'USA',
#     'the danube river': 'germany',
# }
#
# for river, country in rivers_and_countries.items():
#     print(f"{river.title()} runs through {country.title()}.")
#
# print("\nThe countries with some of the popular rivers are:")
# for country in rivers_and_countries.values():
#     print(f"{country.title()}")
#
# print ( "\nThe names of some of the popular rivers are:" )
# for river in rivers_and_countries.keys():
#     print ( f"{river.title()}" )


# favorite_languages = {
# #  'jen': 'python',
# #  'sarah': 'c',
# #  'edward': 'ruby',
# #  'phil': 'python',
# #  }
# #
# # approved_users = ['jen', 'sarah', 'phil', 'muna', 'chinedu', 'amaka']
# #
# # for name in approved_users:
# #     if name in favorite_languages.keys():
# #         print(f"\n{name.title()}, thank you for taking the poll!")
# #     else:
# #         print(f"\n{name.title()}, please take the poll.")

# people = [{'name': 'John', 'age': 32, 'occupation': 'teacher'},
#           {'name': 'Jane', 'age': 28, 'occupation': 'engineer'},
#           {'name': 'Mike', 'age': 45, 'occupation': 'doctor'}]
#
# for person in people:
#     name = person [ 'name' ]
#     age = person [ 'age' ]
#     occupation = person [ 'occupation' ]
#     print(f"Name: {name.title()}\nAge: {age}\nJob: {occupation.title()}")
#     print () # Prints an empty line after each print output.

# pets = [ {'animal': 'dog', 'owner': 'beatrice'},
#          {'animal': 'cat', 'owner': 'victor'},
#          {'animal': 'parrot', 'owner': 'johnson'}]
#
# # Looping through the list to print all the information on each cat.
#
# for pet in pets:
#     animal = pet ['animal']
#     owner = pet ['owner']
#     print(f"\nPet: {animal.title()}\nOwner : {owner.title()}")

# favorite_places = {
#     'Alice': ['Paris', 'New York', 'Sydney'],
#     'Bob': ['London', 'Rome'],
#     'Charlie': ['Tokyo']
# }
#
# for name, places in favorite_places.items():
#     print(f"{name}'s favorite places are:")
#     for place in places:
#         print(f"- {place}")
#     print()
#

# favorite_numbers = {
#     'Alice': [33, 25, 14],
#     'Bob': [45, 23],
#     'Charlie': [52],
# }
#
# for name, numbers in favorite_numbers.items():
#     print(f"\n{name}'s favourite numbers are:")
#     for number in numbers:
#         print(f" - {number}")
#     print()


# cities = {
#     'Abuja': {'country': 'Nigeria', 'population': '200 Million', 'fact': "Abuja is the capital of Nigeria."},
#     'Enugu': {'country': 'Nigeria', 'population': '14 Million', 'fact': 'Enugu is in the eastern region and a nice place.'},
#     'Cross River': {'country': 'Nigeria', 'population': '12 Million', 'fact': "A very popular city with lot's of tourist attractions"},
# }
#
# print ("Cities in Nigeria  and their facts.\n" )
# for city, details in cities.items():
#     country = details['country']
#     population = details['population']
#     fact = details['fact']
#     print(f"{city} is located in {country}.\n"
#           f"It has a  population of {population}.\n"
#           f"{fact}")
#     print()

