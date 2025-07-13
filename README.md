# Library Management System

A complete library management system built in Python that allows tracking books and borrowers with interactive functionality.

## Features

### Book Class
- **Attributes**: `title`, `author`, `is_borrowed` (boolean)
- **Methods**:
  - `mark_as_borrowed()`: Marks a book as borrowed
  - `mark_as_returned()`: Marks a book as returned
  - `__str__()`: String representation showing book status

### LibraryMember Class
- **Attributes**: `name`, `member_id`, `borrowed_books` (list)
- **Methods**:
  - `borrow_book(book)`: Borrows a book if available
  - `return_book(book)`: Returns a borrowed book
  - `list_borrowed_books()`: Lists all borrowed books
  - `__str__()`: String representation of member

## System Requirements

- Python 3.6 or higher
- No external dependencies required

## How to Run

1. Navigate to the project directory
2. Run the system:
   ```bash
   python library_system.py
   ```

## Interactive Menu Options

1. **Display all books** - Shows all books with their availability status
2. **Display all members** - Shows all library members
3. **Borrow a book** - Allows a member to borrow an available book
4. **Return a book** - Allows a member to return a borrowed book
5. **List member's borrowed books** - Shows all books borrowed by a specific member
6. **Exit** - Exits the system

## Sample Data

The system comes pre-loaded with:
- 5 sample books (The Great Gatsby, To Kill a Mockingbird, 1984, Pride and Prejudice, The Hobbit)
- 3 sample members (John Smith, Jane Doe, Bob Johnson)

## Usage Example

```
Welcome to the Library Management System!

==================================================
LIBRARY MANAGEMENT SYSTEM
==================================================
1. Display all books
2. Display all members
3. Borrow a book
4. Return a book
5. List member's borrowed books
6. Exit
==================================================
Enter your choice (1-6): 1

Available Books:
----------------------------------------
1. 'The Great Gatsby' by F. Scott Fitzgerald - Available
2. 'To Kill a Mockingbird' by Harper Lee - Available
3. '1984' by George Orwell - Available
4. 'Pride and Prejudice' by Jane Austen - Available
5. 'The Hobbit' by J.R.R. Tolkien - Available
```

## System Validation

The system includes:
- Input validation for menu choices
- Checks for book availability before borrowing
- Verification that members can only return books they've borrowed
- Clear status messages for all operations

## Code Structure

- **Book Class**: Handles individual book management
- **LibraryMember Class**: Manages member operations and book tracking
- **Main Function**: Provides interactive menu and system coordination
- **Helper Functions**: Support display and input validation

This system demonstrates object-oriented programming principles with proper encapsulation, method implementation, and user interaction. 