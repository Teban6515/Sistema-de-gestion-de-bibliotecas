"""
Queue Data Structure (FIFO)

This module implements a Queue (First In, First Out) data structure.
Used for managing book reservations where first users are served first.

Author: [Your Name]
Date: December 2025
Course: Programming Techniques
"""

class Queue:
    """
    Implementation of a Queue (FIFO - First In, First Out) data structure.
    
    Used for managing book reservations where the first user to request
    a book is served first when the book becomes available.
    
    Attributes:
        items (list): Internal list to store queue elements
        max_size (int): Maximum number of elements (None for unlimited)
    
    Methods:
        enqueue(item): Add an element to the rear of the queue
        dequeue(): Remove and return the front element
        front(): View the front element without removing it
        is_empty(): Check if queue is empty
        size(): Get the number of elements
        clear(): Remove all elements
        to_list(): Convert queue to list
    
    Time Complexity:
        - enqueue(): O(1)
        - dequeue(): O(n) with list, O(1) with deque
        - front(): O(1)
        - is_empty(): O(1)
        - size(): O(1)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self, max_size=None):
        """
        Initialize an empty queue.
        
        Args:
            max_size (int, optional): Maximum queue size. Defaults to None (unlimited).
        
        Raises:
            ValueError: If max_size is negative
        """
        if max_size is not None and max_size < 0:
            raise ValueError("Max size cannot be negative")
        
        self.items = []
        self.max_size = max_size
    
    def enqueue(self, item):
        """
        Add an element to the rear of the queue (FIFO).
        
        Args:
            item: Element to add to the queue
        
        Returns:
            bool: True if successful, False if queue is full
        
        Time Complexity: O(1)
        """
        if self.is_full():
            return False
        
        self.items.append(item)
        return True
    
    def dequeue(self):
        """
        Remove and return the front element from the queue.
        
        Returns:
            Element at the front of the queue
        
        Raises:
            IndexError: If queue is empty
        
        Time Complexity: O(n) due to list shift
        Note: Using collections.deque would make this O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        
        return self.items.pop(0)
    
    def front(self):
        """
        View the front element without removing it.
        
        Returns:
            Element at the front of the queue
        
        Raises:
            IndexError: If queue is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot view front of empty queue")
        
        return self.items[0]
    
    def rear(self):
        """
        View the rear element without removing it.
        
        Returns:
            Element at the rear of the queue
        
        Raises:
            IndexError: If queue is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot view rear of empty queue")
        
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
        
        Time Complexity: O(1)
        """
        return len(self.items) == 0
    
    def is_full(self):
        """
        Check if the queue has reached maximum capacity.
        
        Returns:
            bool: True if queue is full, False otherwise
        
        Time Complexity: O(1)
        """
        if self.max_size is None:
            return False
        return len(self.items) >= self.max_size
    
    def size(self):
        """
        Get the number of elements in the queue.
        
        Returns:
            int: Number of elements
        
        Time Complexity: O(1)
        """
        return len(self.items)
    
    def clear(self):
        """
        Remove all elements from the queue.
        
        Time Complexity: O(1)
        """
        self.items = []
    
    def to_list(self):
        """
        Convert queue to list (front to rear).
        
        Returns:
            list: List representation of queue
        
        Time Complexity: O(n)
        """
        return self.items.copy()
    
    def get_position(self, item):
        """
        Get the position of an item in the queue.
        
        Args:
            item: Item to find
        
        Returns:
            int: Position (0 = front), or -1 if not found
        
        Time Complexity: O(n)
        """
        try:
            return self.items.index(item)
        except ValueError:
            return -1
    
    def to_dict(self):
        """
        Convert queue to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the queue
        """
        return {
            'items': self.items,
            'max_size': self.max_size,
            'size': self.size()
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a Queue from a dictionary.
        
        Args:
            data (dict): Dictionary containing queue data
        
        Returns:
            Queue: New Queue object created from dictionary
        """
        queue = Queue(max_size=data.get('max_size'))
        queue.items = data.get('items', [])
        return queue
    
    def __str__(self):
        """
        String representation of the queue (front to rear).
        
        Returns:
            str: Formatted string showing queue contents
        """
        if self.is_empty():
            return "Queue: [] (empty)"
        
        queue_str = "Queue (front → rear):\n"
        for i, item in enumerate(self.items):
            queue_str += f"  [{i}] {item}\n"
        return queue_str.rstrip()
    
    def __repr__(self):
        """
        Developer-friendly representation.
        
        Returns:
            str: Technical representation of the queue
        """
        return f"Queue(size={self.size()}, max_size={self.max_size})"
    
    def __len__(self):
        """
        Get queue size using len() function.
        
        Returns:
            int: Number of elements in queue
        """
        return len(self.items)
    
    def __iter__(self):
        """
        Make queue iterable (yields from front to rear).
        
        Yields:
            Elements from front to rear
        """
        for item in self.items:
            yield item
    
    def __contains__(self, item):
        """
        Check if item is in the queue.
        
        Args:
            item: Item to search for
        
        Returns:
            bool: True if item is in queue
        """
        return item in self.items


# Example usage and testing
if __name__ == "__main__":
    # Create a queue for book reservations
    reservation_queue = Queue(max_size=10)
    
    print("=== Testing Queue (Book Reservations) ===\n")
    
    # Add reservation requests
    print("Adding reservation requests:")
    reservation_queue.enqueue({"user_id": "U001", "date": "2025-12-01"})
    reservation_queue.enqueue({"user_id": "U002", "date": "2025-12-05"})
    reservation_queue.enqueue({"user_id": "U003", "date": "2025-12-10"})
    
    print(reservation_queue)
    print(f"\nQueue size: {reservation_queue.size()}")
    
    # View next in line
    print(f"\nNext user to be served: {reservation_queue.front()}")
    
    # Serve first in queue
    served = reservation_queue.dequeue()
    print(f"\nServed user: {served}")
    print(f"Queue after serving:")
    print(reservation_queue)
    
    # Test iteration
    print("\nRemaining reservations:")
    for i, reservation in enumerate(reservation_queue, 1):
        print(f"  {i}. {reservation}")
    
    # Test dictionary conversion
    queue_dict = reservation_queue.to_dict()
    print(f"\nDictionary representation: {queue_dict}")
