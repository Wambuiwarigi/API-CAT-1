class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def mark_as_borrowed(self):
        """Mark the book as borrowed"""
        self.is_borrowed = True
        print(f"'{self.title}' has been marked as borrowed.")
    
    def mark_as_returned(self):
        """Mark the book as returned"""
        self.is_borrowed = False
        print(f"'{self.title}' has been marked as returned.")
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        """Borrow a book if it's available"""
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has successfully borrowed '{book.title}'")
            return True
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")
            return False
    
    def return_book(self, book):
        """Return a book"""
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has successfully returned '{book.title}'")
            return True
        else:
            print(f"'{book.title}' is not in {self.name}'s borrowed books list.")
            return False
    
    def list_borrowed_books(self):
        """List all borrowed books"""
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"\n{self.name}'s borrowed books:")
            for i, book in enumerate(self.borrowed_books, 1):
                print(f"{i}. {book.title} by {book.author}")
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Display all books")
    print("2. Display all members")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. List member's borrowed books")
    print("6. Exit")
    print("="*50)


def display_books(books):
    """Display all books with their status"""
    print("\nAvailable Books:")
    print("-" * 40)
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")


def display_members(members):
    """Display all members"""
    print("\nLibrary Members:")
    print("-" * 40)
    for i, member in enumerate(members, 1):
        print(f"{i}. {member}")


def get_valid_choice(prompt, max_value):
    """Get valid user choice"""
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= max_value:
                return choice
            else:
                print(f"Please enter a number between 1 and {max_value}")
        except ValueError:
            print("Please enter a valid number")


def main():
    """Main interactive function"""
   
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
        Book("Pride and Prejudice", "Jane Austen"),
        Book("A Thousand Splendid Suns", "Khaled Hosseini")
    ]
    
    
    members = [
        LibraryMember("John Mwai", "M001"),
        LibraryMember("Joy Warigi", "M002"),
        LibraryMember("Mark Karanja", "M003")
    ]
    
    print("Welcome to the Library Management System!")
    
    while True:
        display_menu()
        choice = get_valid_choice("Enter your choice (1-6): ", 6)
        
        if choice == 1:
            display_books(books)
            
        elif choice == 2:
            display_members(members)
            
        elif choice == 3:
            
            display_books(books)
            book_choice = get_valid_choice("Enter book number to borrow: ", len(books))
            book = books[book_choice - 1]
            
            display_members(members)
            member_choice = get_valid_choice("Enter member number: ", len(members))
            member = members[member_choice - 1]
            
            member.borrow_book(book)
            
        elif choice == 4:
           
            display_members(members)
            member_choice = get_valid_choice("Enter member number: ", len(members))
            member = members[member_choice - 1]
            
            if member.borrowed_books:
                member.list_borrowed_books()
                book_choice = get_valid_choice("Enter book number to return: ", len(member.borrowed_books))
                book = member.borrowed_books[book_choice - 1]
                member.return_book(book)
            else:
                print(f"{member.name} has no books to return.")
                
        elif choice == 5:
            display_members(members)
            member_choice = get_valid_choice("Enter member number: ", len(members))
            member = members[member_choice - 1]
            member.list_borrowed_books()
            
        elif choice == 6:
            print("Thank you for using the Library Management System!")
            break


if __name__ == "__main__":
    main() 