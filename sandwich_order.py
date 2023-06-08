sandwich_orders = ['tuna', 'ham and cheese', 'turkey', 'chicken', 'veggie', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []
print("The Deli has run out of Pastrami")
print(f"I made your Sandwiches: ")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for order in sandwich_orders:
    print(f" - {order.title()}")
    finished_sandwiches.append(order)
for sandwich in finished_sandwiches:
    print(sandwich.title())
    
