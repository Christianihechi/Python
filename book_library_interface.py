from book_library_class import Library

library_name = input("Enter the name of the library: ")
library = Library(library_name)

while True:
    print("\n==== Library Program ====")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Display books")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        book_title = input("Enter the title of the book: ")
        library.add_book(book_title)
    elif choice == "2":
        book_title = input("Enter the title of the book: ")
        library.remove_book(book_title)
    elif choice == "3":
        library.display_books()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
