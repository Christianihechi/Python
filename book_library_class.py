class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title):
        self.books.append(title)
        print(f"Book '{title}' has been added to the library.")

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f"Book '{title}' has been removed from the library.")
        else:
            print(f"Book '{title}' is not found in the library.")

    def display_books(self):
        print("Books available in the library:")
        if self.books:
            for book in self.books:
                print("- " + book)
        else:
            print("No books available in the library.")

