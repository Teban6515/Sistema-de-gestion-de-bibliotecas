"""
Shelf Model

This module defines the Shelf class which represents a physical shelf in the library.
Each shelf has a maximum weight capacity and can hold multiple books.

Author: [Your Name]
Date: December 2025
Course: Programming Techniques
"""

class Shelf:
    """
    Represents a physical shelf in the library.
    
    Attributes:
        shelf_id (str): Unique shelf identifier
        max_weight (float): Maximum weight capacity in kilograms
        books (list): List of Book objects currently on this shelf
        location (str): Physical location in the library
    
    Methods:
        add_book(book): Add a book to the shelf
        remove_book(isbn): Remove a book from the shelf
        get_total_weight(): Calculate total weight of books
        get_total_value(): Calculate total value of books
        is_overloaded(): Check if shelf exceeds weight capacity
        can_add_book(book): Check if book can be added
        to_dict(): Convert shelf to dictionary
        from_dict(data): Create shelf from dictionary
    """
    
    MAX_WEIGHT_CAPACITY = 8.0  # Default maximum weight in Kg
    
    def __init__(self, shelf_id, location="Unknown", max_weight=None):
        """
        Initialize a new Shelf object.
        
        Args:
            shelf_id (str): Unique identifier for the shelf
            location (str, optional): Physical location. Defaults to "Unknown".
            max_weight (float, optional): Max weight capacity. Defaults to 8.0 Kg.
        
        Raises:
            ValueError: If parameters are invalid
        """
        if not shelf_id or not isinstance(shelf_id, str):
            raise ValueError("Shelf ID must be a non-empty string")
        if max_weight is not None and max_weight <= 0:
            raise ValueError("Max weight must be positive")
        
        self.shelf_id = shelf_id
        self.location = location
        self.max_weight = max_weight if max_weight is not None else self.MAX_WEIGHT_CAPACITY
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the shelf if weight capacity allows.
        
        Args:
            book (Book): Book object to add
        
        Returns:
            bool: True if book was added, False if would exceed capacity
        
        Raises:
            ValueError: If book is not a valid Book object
        """
        from .book import Book  # Import here to avoid circular imports
        
        if not isinstance(book, Book):
            raise ValueError("Must provide a valid Book object")
        
        if not self.can_add_book(book):
            return False
        
        self.books.append(book)
        return True
    
    def remove_book(self, isbn):
        """
        Remove a book from the shelf by ISBN.
        
        Args:
            isbn (str): ISBN of the book to remove
        
        Returns:
            Book or None: Removed book object, or None if not found
        """
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                return self.books.pop(i)
        return None
    
    def get_book(self, isbn):
        """
        Get a book from the shelf without removing it.
        
        Args:
            isbn (str): ISBN of the book to find
        
        Returns:
            Book or None: Book object if found, None otherwise
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def get_total_weight(self):
        """
        Calculate the total weight of all books on the shelf.
        
        Returns:
            float: Total weight in kilograms
        """
        return sum(book.weight for book in self.books)
    
    def get_total_value(self):
        """
        Calculate the total value of all books on the shelf.
        
        Returns:
            int: Total value in Colombian pesos (COP)
        """
        return sum(book.value for book in self.books)
    
    def get_remaining_capacity(self):
        """
        Calculate the remaining weight capacity.
        
        Returns:
            float: Remaining capacity in kilograms
        """
        return self.max_weight - self.get_total_weight()
    
    def is_overloaded(self):
        """
        Check if the shelf exceeds its weight capacity.
        
        Returns:
            bool: True if total weight exceeds max_weight
        """
        return self.get_total_weight() > self.max_weight
    
    def can_add_book(self, book):
        """
        Check if a book can be added without exceeding capacity.
        
        Args:
            book (Book): Book object to check
        
        Returns:
            bool: True if book can be added
        """
        return (self.get_total_weight() + book.weight) <= self.max_weight
    
    def get_book_count(self):
        """
        Get the number of books on the shelf.
        
        Returns:
            int: Number of books
        """
        return len(self.books)
    
    def clear(self):
        """
        Remove all books from the shelf.
        
        Returns:
            list: List of removed books
        """
        removed_books = self.books[:]
        self.books = []
        return removed_books
    
    def to_dict(self):
        """
        Convert shelf object to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the shelf
        """
        return {
            'shelf_id': self.shelf_id,
            'location': self.location,
            'max_weight': self.max_weight,
            'books': [book.isbn for book in self.books],  # Store ISBNs only
            'total_weight': self.get_total_weight(),
            'total_value': self.get_total_value()
        }
    
    @staticmethod
    def from_dict(data, book_inventory=None):
        """
        Create a Shelf object from a dictionary.
        
        Args:
            data (dict): Dictionary containing shelf data
            book_inventory (dict, optional): Dictionary mapping ISBN to Book objects
        
        Returns:
            Shelf: New Shelf object created from dictionary
        
        Note:
            If book_inventory is provided, books will be populated from it.
            Otherwise, shelf will be created empty.
        """
        shelf = Shelf(
            shelf_id=data['shelf_id'],
            location=data.get('location', 'Unknown'),
            max_weight=data.get('max_weight', Shelf.MAX_WEIGHT_CAPACITY)
        )
        
        # If book inventory is provided, populate books
        if book_inventory and 'books' in data:
            for isbn in data['books']:
                if isbn in book_inventory:
                    shelf.books.append(book_inventory[isbn])
        
        return shelf
    
    def __str__(self):
        """
        String representation for end users.
        
        Returns:
            str: Formatted string with shelf information
        """
        weight = self.get_total_weight()
        capacity_status = "⚠️ OVERLOADED" if self.is_overloaded() else "✅ OK"
        
        return (f"📚 Shelf {self.shelf_id}\n"
                f"   Location: {self.location}\n"
                f"   Books: {self.get_book_count()}\n"
                f"   Weight: {weight:.2f}/{self.max_weight} Kg {capacity_status}\n"
                f"   Value: ${self.get_total_value():,} COP")
    
    def __repr__(self):
        """
        Developer-friendly representation.
        
        Returns:
            str: Technical representation of the shelf
        """
        return f"Shelf(shelf_id='{self.shelf_id}', books={len(self.books)}, weight={self.get_total_weight():.2f}Kg)"
    
    def __eq__(self, other):
        """
        Compare two shelves for equality based on shelf_id.
        
        Args:
            other (Shelf): Another shelf object
        
        Returns:
            bool: True if shelf_ids are equal
        """
        if not isinstance(other, Shelf):
            return False
        return self.shelf_id == other.shelf_id
    
    def __hash__(self):
        """
        Make Shelf hashable for use in sets and as dict keys.
        
        Returns:
            int: Hash value based on shelf_id
        """
        return hash(self.shelf_id)


# Example usage and testing
if __name__ == "__main__":
    from book import Book  # For testing
    
    # Create a test shelf
    shelf1 = Shelf(
        shelf_id="S-A01",
        location="Aisle A, Row 1",
        max_weight=8.0
    )
    
    print(shelf1)
    print()
    
    # Create some test books
    book1 = Book("978-1", "Book 1", "Author 1", 2.5, 50000)
    book2 = Book("978-2", "Book 2", "Author 2", 3.0, 75000)
    book3 = Book("978-3", "Book 3", "Author 3", 4.0, 100000)
    
    # Add books
    print(f"Adding Book 1 (2.5 Kg): {shelf1.add_book(book1)}")
    print(f"Adding Book 2 (3.0 Kg): {shelf1.add_book(book2)}")
    print(f"Adding Book 3 (4.0 Kg): {shelf1.add_book(book3)}")  # Should fail (would exceed 8 Kg)
    
    print(f"\nShelf after adding books:")
    print(shelf1)
    
    # Test dictionary conversion
    shelf_dict = shelf1.to_dict()
    print(f"\nDictionary: {shelf_dict}")
