# Odd numbers
odd_numbers = list(range(1,30,2))
print(odd_numbers)

odd_numbers = list(range(2,30,2))
print(odd_numbers)


# Step 1: Create an empty list called "squares"
squares = []

# # Step 2: Loop through the numbers 1 to 5
for value in range(1, 6):
    # Step 3: Calculate the square of each number and add it to the "squares" list
    squares.append(value**2)

# Step 4: Print the list of square numbers
print(squares)

# Counting to Twenty
for num in range(1,21):
    print(num)
# Print a list from 1-1000,000
numbers = list(range(1,1001))
for number in numbers:
    print(number)

# Summing a million
numbers = list(range(1, 1000001))
print(f"The minimum is {min(numbers)}." )
print(f"The minimum is {max(numbers)}." )
print(f"The sum is {sum(numbers)}." )

# Odd numbers
odd_numbers = list(range(1,21,2))
for odd in odd_numbers:
    print(odd)

# # Multiples of three
multiples_of_three = list(range(3,60, 3))
for multiples in multiples_of_three:
    print(multiples)


# First 10 Cubes
cubes = []
for i in range(1,11):
    cubes.append(i ** 3)

for cube in cubes:
    print(cube)


cubes = [i**3 for i in range(1,11)]
print(cubes)
