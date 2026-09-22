def display_books(books):
    print("\n--- Library Books ---")

    if not books:
        print("No books available.")
        return

    for title, available in books.items():
        status = "Available" if available else "Borrowed"
        print(f"{title} - {status}")


books = {
    "Python Basics": True,
    "Clean Code": True,
    "Computer Networks": False
}

while True:
    print("\n1. View books")
    print("2. Search book")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        display_books(books)

    elif choice == "2":
        title = input("Enter book title: ")

        if title in books:
            status = "Available" if books[title] else "Borrowed"
            print(f"{title}: {status}")
        else:
            print("Book not found.")

    elif choice == "3":
        title = input("Enter book title: ")

        if title not in books:
            print("Book not found.")
        elif not books[title]:
            print("Book is already borrowed.")
        else:
            books[title] = False
            print("Book borrowed successfully.")

    elif choice == "4":
        title = input("Enter book title: ")

        if title not in books:
            print("Book not found.")
        elif books[title]:
            print("Book is already available.")
        else:
            books[title] = True
            print("Book returned successfully.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
