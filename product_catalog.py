class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Method to add a product to the catalog
    def add_product(self, catalog):
        catalog[self.name] = self

    # Method to remove a product from the catalog
    def remove_product(self, catalog, remove):
        if remove in catalog:
            del catalog[remove]
            print(f"{remove} removed from the catalog.")
        else:
            print(f"{remove} is not in the catalog.")

    # Method to display the product catalog
    def show_products(self, catalog):
        print("=== Product Catalog ===")
        for product in catalog.values():
            print(f"Name: {product.name}")
            print(f"Price: {product.price}")
            print(f"Quantity: {product.quantity}")
            print()

# Create an empty catalog
catalog = {}

print("1. Add Product")
print("2. Remove Product")
print("3. View Product Catalog")
print("4. Exit")

while True:
    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == '1':
        name = input("Enter product name: ")
        price = float(input("Enter product's price: "))
        quantity = int(input("Enter product's quantity: "))

        product = Product(name, price, quantity)
        product.add_product(catalog)

        print(f"{name} added to the catalog.\n")

    elif choice == '2':
        if not catalog:
            print("There are no products in the catalog.\n")
            continue

        remove = input("Enter product to remove: ")
        product = Product(remove, 0, 0)
        product.remove_product(catalog, remove)

    elif choice == '3':
        if not catalog:
            print("There are no products in the catalog.\n")
            continue

        product = Product('', 0, 0)
        product.show_products(catalog)

    elif choice == '4':
        print("Program closed!")
        break

    else:
        print("Invalid choice. Please try again.\n")
