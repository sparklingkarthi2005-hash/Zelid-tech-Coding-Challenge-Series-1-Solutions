# A global list to hold all book dictionaries
library = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    # Create a simple dictionary for the new book
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    library.append(new_book)
    print("Book added successfully!")

def display_books():
    if len(library) == 0:
        print("No books in the library.")
    else:
        print("\n--- List of Books ---")
        for book in library:
            if book["available"] == True:
                status = "Available"
            else:
                status = "Issued"
            print("ID:", book["id"], "| Title:", book["title"], "| Author:", book["author"], "| Status:", status)

def search_book():
    query = input("Enter Book ID or Book Name to search: ")
    found = False

    for book in library:
        if book["id"] == query or book["title"] == query:
            if book["available"] == True:
                status = "Available"
            else:
                status = "Issued"
            print("Found -> ID:", book["id"], "| Title:", book["title"], "| Author:", book["author"], "| Status:", status)
            found = True

    if found == False:
        print("Book not found.")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    found = False
    
    for book in library:
        if book["id"] == book_id:
            found = True
            if book["available"] == True:
                book["available"] = False
                print("Book issued successfully!")
            else:
                print("Sorry, this book is already issued to someone else.")
                
    if found == False:
        print("Book ID not found.")

def return_book():
    book_id = input("Enter Book ID to return: ")
    found = False

    for book in library:
        if book["id"] == book_id:
            found = True
            if book["available"] == False:
                book["available"] = True
                print("Book returned successfully!")
            else:
                print("This book was not issued.")

    if found == False:
        print("Book ID not found.")

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    found = False

    for book in library:
        if book["id"] == book_id:
            library.remove(book)
            print("Book deleted successfully!")
            found = True
            break  # Exit loop after deleting

    if found == False:
        print("Book ID not found.")

# Main Program Menu Loop
while True:
    print("\n=== LIBRARY MENU ===")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter choice (1-7): ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
