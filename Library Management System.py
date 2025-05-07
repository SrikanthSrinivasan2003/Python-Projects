class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\n Available Books:")
        for idx, book in enumerate(self.books):
            print(f"{idx + 1}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed '{book.title}'")
                return
        print("Book not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f"Book '{book.title}' returned. Thanks!")
                return
        print("Book not found or not borrowed.")


class UserInterface:
    def __init__(self):
        self.library = Library()

    def show_menu(self):
        while True:
            print("\n==== Library Management System ====")
            print("1. Add Book")
            print("2. Display Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")
            choice = input("Enter choice (1-5): ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                self.library.add_book(title, author)

            elif choice == '2':
                self.library.display_books()

            elif choice == '3':
                title = input("Enter book title to borrow: ")
                self.library.borrow_book(title)

            elif choice == '4':
                title = input("Enter book title to return: ")
                self.library.return_book(title)

            elif choice == '5':
                print("Exiting Library System. Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = UserInterface()
    app.show_menu()
