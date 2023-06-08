# Define a list of sandwich orders
sandwich_orders = ['tuna', 'ham and cheese', 'turkey', 'chicken', 'veggie', 'pastrami', 'pastrami', 'pastrami']

# Create an empty list to store finished sandwiches
finished_sandwiches = []

# Print a message indicating that the Deli has run out of Pastrami
print("The Deli has run out of Pastrami")

# Print a message indicating the sandwiches that have been made
print("I made your sandwiches:")

# Remove all occurrences of 'pastrami' from the sandwich orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Iterate over the remaining sandwich orders and print each order
for order in sandwich_orders:
    print(f" - {order.title()}")
    finished_sandwiches.append(order)

# Print the title-cased finished sandwiches
for sandwich in finished_sandwiches:
    print(sandwich.title())
