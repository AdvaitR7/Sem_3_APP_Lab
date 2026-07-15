# Write a program to create a simplified library management system using OOP Principles in python. This system should manage books and patrons (Library users), allowing for basic operations such as adding new books, registering patrons, borrowing books, and returning books.
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("----------------------")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False

    def display_info(self):
        print(f"Patron ID: {self.patron_id}")
        print(f"Name: {self.name}")

        if len(self.borrowed_books) == 0:
            print("Borrowed Books: None")
        else:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")

        print("----------------------")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_patron(self, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None

    def borrow_book(self, book_id, patron_id):
        book = self.find_book(book_id)
        patron = self.find_patron(patron_id)

        if book is None:
            print("Book not found.")
            return

        if patron is None:
            print("Patron not found.")
            return

        if book.borrow():
            patron.borrow_book(book)
            print(f"{patron.name} borrowed '{book.title}'.")
        else:
            print("Book is already borrowed.")

    def return_book(self, book_id, patron_id):
        book = self.find_book(book_id)
        patron = self.find_patron(patron_id)

        if book is None:
            print("Book not found.")
            return

        if patron is None:
            print("Patron not found.")
            return

        if patron.return_book(book):
            book.return_book()
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("This patron did not borrow this book.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            print("\nLibrary Books:")
            print("======================")
            for book in self.books:
                book.display_info()

    def display_patrons(self):
        if len(self.patrons) == 0:
            print("No patrons registered.")
        else:
            print("\nRegistered Patrons:")
            print("======================")
            for patron in self.patrons:
                patron.display_info()


# Main program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        patron_id = int(input("Enter Patron ID: "))
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        library.register_patron(patron)

    elif choice == "3":
        book_id = int(input("Enter Book ID to borrow: "))
        patron_id = int(input("Enter Patron ID: "))

        library.borrow_book(book_id, patron_id)

    elif choice == "4":
        book_id = int(input("Enter Book ID to return: "))
        patron_id = int(input("Enter Patron ID: "))

        library.return_book(book_id, patron_id)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_patrons()

    elif choice == "7":
        print("Exiting Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")