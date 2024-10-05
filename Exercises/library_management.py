books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"},
    {"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Checked Out"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "status": "Available"},
]

users = [
    {"id": 1, "name": "Talha", "borrowed_books": []},
    {"id": 2, "name": "Wajih", "borrowed_books": []},
]

# Books view

def view_books():
    """Displays all books in the library."""
    print("\nAll Books:")
    for book in books:
        print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')
    print("----------------------------------------")

def view_available_books():
    """Displays only available books."""
    print("\nAvailable Books:")
    for book in books:
        if book["status"] == "Available":
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]}')
    print("----------------------------------------")

def view_checked_out_books():
    """Displays only checked-out books."""
    print("\nChecked-Out Books:")
    for book in books:
        if book["status"] == "Checked Out":
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]}')
    print("----------------------------------------")

def search_books():
    """Searches books by title, author, or genre."""
    search_type = input("\nSearch by (title/author/genre): ").strip().lower()
    query = input(f"Enter the {search_type}: ").strip().lower()

    print("\nSearch Results:")
    for book in books:
        if query in book[search_type].lower():
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')
    print("----------------------------------------")

def borrow_book(user_id):
    """Allows a user to borrow a book if it is available."""
    book_id = int(input("\nEnter the Book ID you want to borrow: "))

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                for user in users:
                    if user["id"] == user_id:
                        user["borrowed_books"].append(book["title"])
                        book["status"] = "Checked Out"
                        print(f'You have successfully borrowed "{book["title"]}".')
                        return
            else:
                print(f'Sorry, the book "{book["title"]}" is currently checked out.')
                return
    print("Invalid book ID.")
    print("----------------------------------------")

def return_book(user_id):
    """Allows a user to return a borrowed book."""
    book_id = int(input("\nEnter the Book ID you want to return: "))

    for book in books:
        if book["id"] == book_id:
            for user in users:
                if user["id"] == user_id:
                    if book["title"] in user["borrowed_books"]:
                        user["borrowed_books"].remove(book["title"])
                        book["status"] = "Available"
                        print(f'You have successfully returned "{book["title"]}".')
                        return
    print("Invalid book ID or you haven't borrowed this book.")
    print("----------------------------------------")

def view_users():
    """Displays all users and their borrowed books."""
    print("\nUsers:")
    for user in users:
        print(f'User {user["id"]}: {user["name"]}')
        if user["borrowed_books"]:
            print("  Borrowed Books:", ", ".join(user["borrowed_books"]))
        else:
            print("  No borrowed books.")
    print("----------------------------------------")

# Main Menu

def main_menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("----------------------------------------")
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            view_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            user_id = int(input("\nEnter your User ID: "))
            borrow_book(user_id)
        elif choice == "4":
            user_id = int(input("\nEnter your User ID: "))
            return_book(user_id)
        elif choice == "5":
            view_users()
        elif choice == "6":
            print("Thank you for using the Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print("----------------------------------------")

# run program
main_menu()
