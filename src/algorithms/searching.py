"""
Searching Algorithms

This module implements searching algorithms required for the Library Management System:
- Linear Search: For searching by title or author in unsorted inventory
- Binary Search: For searching by ISBN in sorted inventory (CRITICAL)

Author: [Your Name]
Date: December 2025
Course: Programming Techniques
"""

def linear_search_by_title(books_list, title):
    """
    Search for books by title using Linear Search algorithm.
    
    Searches through the General Inventory (unsorted list) to find
    books matching the given title. Search is case-insensitive and
    supports partial matches.
    
    Args:
        books_list (list): List of Book objects (unsorted)
        title (str): Title to search for (partial match allowed)
    
    Returns:
        list: List of matching Book objects
    
    Time Complexity: O(n) - must check every element
    Space Complexity: O(k) - where k is number of matches
    
    Algorithm:
        1. Iterate through entire list
        2. Compare each book's title with search term
        3. Add matches to result list
        4. Return all matches
    """
    matches = []
    title_lower = title.lower()
    
    for book in books_list:
        if title_lower in book.title.lower():
            matches.append(book)
    
    return matches


def linear_search_by_author(books_list, author):
    """
    Search for books by author using Linear Search algorithm.
    
    Searches through the General Inventory to find all books
    by a specific author. Search is case-insensitive and
    supports partial matches.
    
    Args:
        books_list (list): List of Book objects (unsorted)
        author (str): Author name to search for (partial match allowed)
    
    Returns:
        list: List of matching Book objects
    
    Time Complexity: O(n)
    Space Complexity: O(k) where k is number of matches
    """
    matches = []
    author_lower = author.lower()
    
    for book in books_list:
        if author_lower in book.author.lower():
            matches.append(book)
    
    return matches


def linear_search_by_isbn(books_list, isbn):
    """
    Search for a book by exact ISBN using Linear Search.
    
    Args:
        books_list (list): List of Book objects
        isbn (str): Exact ISBN to search for
    
    Returns:
        int: Index of book if found, -1 if not found
    
    Time Complexity: O(n)
    """
    for i, book in enumerate(books_list):
        if book.isbn == isbn:
            return i
    return -1

### Encontrar la posición de un libro en una lista ordenada usando su ISBN.
def binary_search_by_isbn(sorted_books, isbn):

    left = 0
    right = len(sorted_books) - 1
    
    while left <= right:
        # Calculate middle index
        mid = (left + right) // 2
        mid_isbn = sorted_books[mid].isbn
        
        # Check if we found the book
        if mid_isbn == isbn:
            return mid
        
        # If target is less than middle, search left half
        elif isbn < mid_isbn:
            right = mid - 1
        
        # If target is greater than middle, search right half
        else:
            left = mid + 1
    
    # Book not found
    return -1


def binary_search_recursive(sorted_books, isbn, left=0, right=None):
    """
    Recursive implementation of Binary Search by ISBN.
    
    Alternative implementation using recursion instead of iteration.
    Demonstrates recursive divide-and-conquer approach.
    
    Args:
        sorted_books (list): Sorted list of Book objects
        isbn (str): ISBN to search for
        left (int): Left boundary of search range
        right (int): Right boundary of search range
    
    Returns:
        int: Index if found, -1 if not found
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) - due to recursion call stack
    """
    # Initialize right boundary on first call
    if right is None:
        right = len(sorted_books) - 1
    
    # Base case: range is invalid
    if left > right:
        return -1
    
    # Calculate middle
    mid = (left + right) // 2
    mid_isbn = sorted_books[mid].isbn
    
    # Base case: found the book
    if mid_isbn == isbn:
        return mid
    
    # Recursive case: search left half
    elif isbn < mid_isbn:
        return binary_search_recursive(sorted_books, isbn, left, mid - 1)
    
    # Recursive case: search right half
    else:
        return binary_search_recursive(sorted_books, isbn, mid + 1, right)


def verify_book_has_reservations(sorted_books, isbn, reservation_queue):
    """
    CRITICAL FUNCTION: Verify if a returned book has pending reservations.
    
    This function uses Binary Search to find the book in the Sorted Inventory,
    then checks if there are pending reservations for it.
    
    Workflow:
        1. Use binary search to find book by ISBN
        2. If book exists, check reservation queue
        3. Return reservation info if exists
    
    Args:
        sorted_books (list): Sorted inventory list
        isbn (str): ISBN of returned book
        reservation_queue (dict): Dictionary mapping ISBN to Queue of reservations
    
    Returns:
        tuple: (book_index, has_reservations, next_user)
            - book_index (int): Index in sorted inventory (-1 if not found)
            - has_reservations (bool): True if reservations exist
            - next_user (str or None): User ID of next reservation
    """
    # Use binary search to find book
    book_index = binary_search_by_isbn(sorted_books, isbn)
    
    if book_index == -1:
        return (-1, False, None)
    
    # Check if there are reservations for this book
    if isbn in reservation_queue and not reservation_queue[isbn].is_empty():
        # Get next user in queue without removing
        next_reservation = reservation_queue[isbn].front()
        next_user = next_reservation.get('user_id')
        return (book_index, True, next_user)
    
    return (book_index, False, None)


# Testing module
if __name__ == "__main__":
    import sys
    sys.path.append('../..')
    from src.models.book import Book
    from src.algorithms.sorting import insertion_sort_by_isbn
    
    # Create test books
    books = [
        Book("978-0-13-468599-1", "Clean Code", "Robert C. Martin", 0.8, 125000, 3),
        Book("978-0-201-61622-4", "The Pragmatic Programmer", "Andrew Hunt", 0.65, 110000, 2),
        Book("978-0-13-235088-4", "Clean Architecture", "Robert C. Martin", 0.75, 135000, 2),
        Book("978-0-262-03384-8", "Introduction to Algorithms", "Thomas H. Cormen", 1.5, 195000, 3),
    ]
    
    print("=== Testing Search Algorithms ===\n")
    
    # Test Linear Search
    print("Linear Search by Author (Robert):")
    results = linear_search_by_author(books, "Robert")
    for book in results:
        print(f"  {book.title} by {book.author}")
    
    print("\nLinear Search by Title (Clean):")
    results = linear_search_by_title(books, "Clean")
    for book in results:
        print(f"  {book.title}")
    
    # Test Binary Search
    sorted_books = books.copy()
    insertion_sort_by_isbn(sorted_books)
    
    print("\nSorted books by ISBN:")
    for book in sorted_books:
        print(f"  {book.isbn} - {book.title}")
    
    print("\nBinary Search for ISBN '978-0-262-03384-8':")
    index = binary_search_by_isbn(sorted_books, "978-0-262-03384-8")
    if index != -1:
        print(f"  Found at index {index}: {sorted_books[index].title}")
    else:
        print("  Not found")
    
    print("\nBinary Search for non-existent ISBN '978-9-99-999999-9':")
    index = binary_search_by_isbn(sorted_books, "978-9-99-999999-9")
    print(f"  Result: {index}")
