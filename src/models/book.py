"""
Book Model

This module defines the Book class which represents a book in the library inventory.
Each book has attributes like ISBN, title, author, weight, value, and stock.

Author: [Your Name]
Date: December 2025
Course: Programming Techniques
"""

class Book:
    """
    Represents a book in the library inventory.
    
    Attributes:
        isbn (str): International Standard Book Number (unique identifier)
        title (str): Book title
        author (str): Book author's full name
        weight (float): Book weight in kilograms
        value (int): Book value in Colombian pesos (COP)
        stock (int): Number of copies available in inventory
        category (str): Book category/genre (optional)
        publisher (str): Publishing company (optional)
        year (int): Publication year (optional)
    
    Methods:
        to_dict(): Convert book object to dictionary
        from_dict(data): Create book object from dictionary
        __str__(): String representation of the book
        __repr__(): Developer-friendly representation
        __eq__(): Compare books by ISBN
        __lt__(): Compare books for sorting by ISBN
    """
    
    def __init__(self, isbn, title, author, weight, value, stock=1, 
                 category="General", publisher="Unknown", year=2024):
        """
        Initialize a new Book object.
        
        Args:
            isbn (str): International Standard Book Number
            title (str): Book title
            author (str): Author's full name
            weight (float): Weight in kilograms
            value (int): Value in Colombian pesos
            stock (int, optional): Number of copies available. Defaults to 1.
            category (str, optional): Book category. Defaults to "General".
            publisher (str, optional): Publisher name. Defaults to "Unknown".
            year (int, optional): Publication year. Defaults to 2024.
        
        Raises:
            ValueError: If any required parameter is invalid
        """
        # Validation
        if not isbn or not isinstance(isbn, str):
            raise ValueError("ISBN must be a non-empty string")
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")
        if not author or not isinstance(author, str):
            raise ValueError("Author must be a non-empty string")
        if weight <= 0:
            raise ValueError("Weight must be positive")
        if value < 0:
            raise ValueError("Value cannot be negative")
        if stock < 0:
            raise ValueError("Stock cannot be negative")
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.weight = float(weight)
        self.value = int(value)
        self.stock = int(stock)
        self.category = category
        self.publisher = publisher
        self.year = int(year)
    
    def is_available(self):
        """
        Check if the book is available for loan.
        
        Returns:
            bool: True if stock > 0, False otherwise
        """
        return self.stock > 0
    
    def decrease_stock(self):
        """
        Decrease stock by 1 when book is loaned.
        
        Returns:
            bool: True if successful, False if no stock available
        """
        if self.stock > 0:
            self.stock -= 1
            return True
        return False
    
    def increase_stock(self):
        """
        Increase stock by 1 when book is returned.
        """
        self.stock += 1
    
    def to_dict(self):
        """
        Convert book object to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the book
        """
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'weight': self.weight,
            'value': self.value,
            'stock': self.stock,
            'category': self.category,
            'publisher': self.publisher,
            'year': self.year
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a Book object from a dictionary.
        
        Args:
            data (dict): Dictionary containing book data
        
        Returns:
            Book: New Book object created from dictionary
        
        Raises:
            KeyError: If required keys are missing
        """
        return Book(
            isbn=data['isbn'],
            title=data['title'],
            author=data['author'],
            weight=data['weight'],
            value=data['value'],
            stock=data.get('stock', 1),
            category=data.get('category', 'General'),
            publisher=data.get('publisher', 'Unknown'),
            year=data.get('year', 2024)
        )
    
    def __str__(self):
        """
        String representation for end users.
        
        Returns:
            str: Formatted string with book information
        """
        return (f"📚 {self.title}\n"
                f"   Author: {self.author}\n"
                f"   ISBN: {self.isbn}\n"
                f"   Value: ${self.value:,} COP\n"
                f"   Stock: {self.stock} copies")
    
    def __repr__(self):
        """
        Developer-friendly representation.
        
        Returns:
            str: Technical representation of the book
        """
        return f"Book(isbn='{self.isbn}', title='{self.title}', stock={self.stock})"
    
    def __eq__(self, other):
        """
        Compare two books for equality based on ISBN.
        
        Args:
            other (Book): Another book object
        
        Returns:
            bool: True if ISBNs are equal
        """
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn
    
    def __lt__(self, other):
        """
        Compare two books for sorting by ISBN (ascending).
        
        Args:
            other (Book): Another book object
        
        Returns:
            bool: True if this book's ISBN < other's ISBN
        """
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn < other.isbn
    
    def __hash__(self):
        """
        Make Book hashable for use in sets and as dict keys.
        
        Returns:
            int: Hash value based on ISBN
        """
        return hash(self.isbn)


# Example usage and testing
if __name__ == "__main__":
    # Create a test book
    book1 = Book(
        isbn="978-0-13-468599-1",
        title="Clean Code: A Handbook of Agile Software Craftsmanship",
        author="Robert C. Martin",
        weight=0.8,
        value=125000,
        stock=3,
        category="Programming",
        publisher="Prentice Hall",
        year=2008
    )
    
    print(book1)
    print(f"\nAvailable: {book1.is_available()}")
    
    # Test dictionary conversion
    book_dict = book1.to_dict()
    print(f"\nDictionary: {book_dict}")
    
    # Test creating from dictionary
    book2 = Book.from_dict(book_dict)
    print(f"\nRecreated: {book2}")
    
    # Test comparison
    print(f"\nAre they equal? {book1 == book2}")
