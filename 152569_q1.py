# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (Borrowed: {'Yes' if self.is_borrowed else 'No'})"


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"Books borrowed by {self.name}:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")


# Interactive code to allow a member to borrow and return books
def main():
    # Creating some sample books
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
        Book("These Precious Days", "Ann Patchett"),
        Book("Love and Other Words", "Christina Lauren"),
        Book("Mere Christianity", "C.S. Lewis"),
        Book("The Girl on the Train", "Paula Hawkins"),
    ]

    # Creating library members
    members = {
        "M001": LibraryMember("Alice", "M001"),
        "M002": LibraryMember("Patriciah", "M002"),
        "M003": LibraryMember("John", "M003"),
        "M004": LibraryMember("Alex", "M004"),
        "M005": LibraryMember("Grace", "M005"),
    }

    # Menu for interaction
    while True:
        print("\nLibrary Management System")
        print("1. Select a member")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. List borrowed books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable members:")
            for member_id, member in members.items():
                print(f"{member_id}: {member.name}")
            member_id = input("Enter the member ID to select: ")
            if member_id in members:
                member = members[member_id]
                print(f"Selected member: {member.name}")
            else:
                print("Invalid member ID. Try again.")

        elif choice == "2":
            print("\nAvailable books:")
            available_books = [book for book in books if not book.is_borrowed]
            for idx, book in enumerate(available_books, start=1):
                print(f"{idx}. {book}")
            book_choice = int(input("Enter the number of the book to borrow: ")) - 1
            if 0 <= book_choice < len(available_books):
                member.borrow_book(available_books[book_choice])
            else:
                print("Invalid choice. Try again.")

        elif choice == "3":
            if member.borrowed_books:
                print("\nBorrowed books:")
                for idx, book in enumerate(member.borrowed_books, start=1):
                    print(f"{idx}. {book}")
                book_choice = int(input("Enter the number of the book to return: ")) - 1
                if 0 <= book_choice < len(member.borrowed_books):
                    member.return_book(member.borrowed_books[book_choice])
                else:
                    print("Invalid choice. Try again.")
            else:
                print("No books to return.")

        elif choice == "4":
            member.list_borrowed_books()

        elif choice == "5":
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please select again.")

# Run the interactive session
if __name__ == "__main__":
    main()
