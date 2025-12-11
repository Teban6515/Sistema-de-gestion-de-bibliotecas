"""
Stack Data Structure (LIFO)

This module implements a Stack (Last In, First Out) data structure.
Used for managing loan history where recent loans are accessed first.

Author: [Your Name]
Date: December 2025
Course: Programming Techniques
"""

class Stack:
    """
    Implementation of a Stack (LIFO - Last In, First Out) data structure.
    
    Used for managing loan history where the most recent loans are
    accessed first (stack of loan records per user).
    
    Attributes:
        items (list): Internal list to store stack elements
        max_size (int): Maximum number of elements (None for unlimited)
    
    Methods:
        push(item): Add an element to the top of the stack
        pop(): Remove and return the top element
        peek(): View the top element without removing it
        is_empty(): Check if stack is empty
        size(): Get the number of elements
        clear(): Remove all elements
        to_list(): Convert stack to list
    
    Time Complexity:
        - push(): O(1)
        - pop(): O(1)
        - peek(): O(1)
        - is_empty(): O(1)
        - size(): O(1)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self, max_size=None):
        """
        Initialize an empty stack.
        
        Args:
            max_size (int, optional): Maximum stack size. Defaults to None (unlimited).
        
        Raises:
            ValueError: If max_size is negative
        """
        if max_size is not None and max_size < 0:
            raise ValueError("Max size cannot be negative")
        
        self.items = []
        self.max_size = max_size
    
    def push(self, item):
        """
        Add an element to the top of the stack (LIFO).
        
        Args:
            item: Element to add to the stack
        
        Returns:
            bool: True if successful, False if stack is full
        
        Time Complexity: O(1)
        """
        if self.is_full():
            return False
        
        self.items.append(item)
        return True
    
    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Returns:
            Element at the top of the stack
        
        Raises:
            IndexError: If stack is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        
        return self.items.pop()
    
    def peek(self):
        """
        View the top element without removing it.
        
        Returns:
            Element at the top of the stack
        
        Raises:
            IndexError: If stack is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek at empty stack")
        
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
        
        Time Complexity: O(1)
        """
        return len(self.items) == 0
    
    def is_full(self):
        """
        Check if the stack has reached maximum capacity.
        
        Returns:
            bool: True if stack is full, False otherwise
        
        Time Complexity: O(1)
        """
        if self.max_size is None:
            return False
        return len(self.items) >= self.max_size
    
    def size(self):
        """
        Get the number of elements in the stack.
        
        Returns:
            int: Number of elements
        
        Time Complexity: O(1)
        """
        return len(self.items)
    
    def clear(self):
        """
        Remove all elements from the stack.
        
        Time Complexity: O(1)
        """
        self.items = []
    
    def to_list(self):
        """
        Convert stack to list (top to bottom).
        
        Returns:
            list: List representation of stack (most recent first)
        
        Time Complexity: O(n)
        """
        return self.items[::-1]  # Reverse to show top first
    
    def to_dict(self):
        """
        Convert stack to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the stack
        """
        return {
            'items': self.items,
            'max_size': self.max_size,
            'size': self.size()
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a Stack from a dictionary.
        
        Args:
            data (dict): Dictionary containing stack data
        
        Returns:
            Stack: New Stack object created from dictionary
        """
        stack = Stack(max_size=data.get('max_size'))
        stack.items = data.get('items', [])
        return stack
    
    def __str__(self):
        """
        String representation of the stack (top to bottom).
        
        Returns:
            str: Formatted string showing stack contents
        """
        if self.is_empty():
            return "Stack: [] (empty)"
        
        stack_str = "Stack (top → bottom):\n"
        for i, item in enumerate(reversed(self.items)):
            stack_str += f"  [{i}] {item}\n"
        return stack_str.rstrip()
    
    def __repr__(self):
        """
        Developer-friendly representation.
        
        Returns:
            str: Technical representation of the stack
        """
        return f"Stack(size={self.size()}, max_size={self.max_size})"
    
    def __len__(self):
        """
        Get stack size using len() function.
        
        Returns:
            int: Number of elements in stack
        """
        return len(self.items)
    
    def __iter__(self):
        """
        Make stack iterable (yields from top to bottom).
        
        Yields:
            Elements from top to bottom
        """
        for item in reversed(self.items):
            yield item
    
    def __contains__(self, item):
        """
        Check if item is in the stack.
        
        Args:
            item: Item to search for
        
        Returns:
            bool: True if item is in stack
        """
        return item in self.items


# Example usage and testing
if __name__ == "__main__":
    # Create a stack for loan history
    loan_history = Stack(max_size=10)
    
    print("=== Testing Stack (Loan History) ===\n")
    
    # Add loan records
    print("Adding loan records:")
    loan_history.push({"isbn": "978-1", "date": "2025-12-01"})
    loan_history.push({"isbn": "978-2", "date": "2025-12-05"})
    loan_history.push({"isbn": "978-3", "date": "2025-12-10"})
    
    print(loan_history)
    print(f"\nStack size: {loan_history.size()}")
    
    # Peek at most recent loan
    print(f"\nMost recent loan: {loan_history.peek()}")
    
    # Pop (return a book)
    returned = loan_history.pop()
    print(f"\nReturned book: {returned}")
    print(f"Stack after return:")
    print(loan_history)
    
    # Test iteration
    print("\nIterating through loan history:")
    for i, loan in enumerate(loan_history, 1):
        print(f"  {i}. {loan}")
    
    # Test dictionary conversion
    stack_dict = loan_history.to_dict()
    print(f"\nDictionary representation: {stack_dict}")
