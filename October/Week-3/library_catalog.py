class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f'You borrowed "{self.title}".')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f'You returned "{self.title}".')
        else:
            print(f'"{self.title}" was not borrowed.')

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"{self.title} by {self.author} | {status}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added to {self.name}.')

    def display_books(self):
        print(f"\n--- {self.name} Catalogue ---")

        if not self.books:
            print("No books in the catalogue.")
            return

        for book in self.books:
            book.display_info()


# Create objects
library = Library("Campus Library")

book1 = Book("Python Basics", "John Smith")
book2 = Book("Object-Oriented Programming", "Sarah Jones")

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# Display the catalogue
library.display_books()

# Borrow and return a book
print("\n--- Borrowing Books ---")
book1.borrow()
book1.borrow()

print("\n--- Returning Book ---")
book1.return_book()

# Display the updated catalogue
library.display_books()
