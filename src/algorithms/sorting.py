"""
Sorting Algorithms

This module implements sorting algorithms required for the Library Management System:
- Insertion Sort: For maintaining sorted inventory
- Merge Sort: For generating reports sorted by value

Author: [Your Name]
Date: December 2025
Course: Programming Techniques
"""

def insertion_sort_by_isbn(books_list):
    """
    Sort a list of Book objects by ISBN using Insertion Sort algorithm.
    
    This algorithm is used to maintain the Sorted Inventory every time
    a new book is added to the system. It's efficient for nearly sorted data.
    
    Args:
        books_list (list): List of Book objects to sort
    
    Returns:
        list: The same list, sorted in-place by ISBN (ascending)
    
    Time Complexity:
        - Best case: O(n) - Already sorted
        - Average case: O(n²)
        - Worst case: O(n²) - Reverse sorted
    
    Space Complexity: O(1) - In-place sorting
    
    Stability: Stable - preserves relative order of equal elements
    
    Algorithm:
        1. Start from second element
        2. Compare with elements to its left
        3. Shift larger elements one position right
        4. Insert current element in correct position
        5. Repeat until all elements are sorted
    """
    n = len(books_list)
    
    # Traverse from second element to end
    for i in range(1, n):
        key = books_list[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and books_list[j].isbn > key.isbn:
            books_list[j + 1] = books_list[j]
            j -= 1
        
        # Insert key at correct position
        books_list[j + 1] = key
    
    return books_list


def insertion_sort_by_value(books_list):
    """
    Sort a list of Book objects by value using Insertion Sort algorithm.
    
    Args:
        books_list (list): List of Book objects to sort
    
    Returns:
        list: The same list, sorted in-place by value (ascending)
    
    Time Complexity: O(n²) average and worst case
    Space Complexity: O(1)
    """
    n = len(books_list)
    
    for i in range(1, n):
        key = books_list[i]
        j = i - 1
        
        while j >= 0 and books_list[j].value > key.value:
            books_list[j + 1] = books_list[j]
            j -= 1
        
        books_list[j + 1] = key
    
    return books_list


def merge_sort_by_value(books_list):
    """
    Sort a list of Book objects by value using Merge Sort algorithm.
    
    This algorithm is used to generate the Global Inventory Report
    sorted by Value (COP). It guarantees O(n log n) performance.
    
    Args:
        books_list (list): List of Book objects to sort
    
    Returns:
        list: New sorted list by value (descending for reports)
    
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n) - requires additional space for merging
    
    Stability: Stable - preserves relative order of equal elements
    
    Algorithm (Divide and Conquer):
        1. Divide: Split list into two halves
        2. Conquer: Recursively sort each half
        3. Combine: Merge the sorted halves
    """
    # Base case: list with 0 or 1 element is already sorted
    if len(books_list) <= 1:
        return books_list
    
    # Divide: Find middle point
    mid = len(books_list) // 2
    left_half = books_list[:mid]
    right_half = books_list[mid:]
    
    # Conquer: Recursively sort both halves
    left_sorted = merge_sort_by_value(left_half)
    right_sorted = merge_sort_by_value(right_half)
    
    # Combine: Merge the sorted halves
    return merge_by_value(left_sorted, right_sorted)


def merge_by_value(left, right):
    """
    Merge two sorted lists into one sorted list by value (descending).
    
    Args:
        left (list): First sorted list of Book objects
        right (list): Second sorted list of Book objects
    
    Returns:
        list: Merged sorted list (descending by value)
    
    Time Complexity: O(n + m) where n, m are lengths of input lists
    Space Complexity: O(n + m)
    """
    result = []
    i = j = 0
    
    # Compare elements and merge in descending order (higher value first)
    while i < len(left) and j < len(right):
        if left[i].value >= right[j].value:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements from left
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Append remaining elements from right
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


def merge_sort_by_isbn(books_list):
    """
    Sort a list of Book objects by ISBN using Merge Sort algorithm.
    
    Args:
        books_list (list): List of Book objects to sort
    
    Returns:
        list: New sorted list by ISBN (ascending)
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(books_list) <= 1:
        return books_list
    
    mid = len(books_list) // 2
    left = merge_sort_by_isbn(books_list[:mid])
    right = merge_sort_by_isbn(books_list[mid:])
    
    return merge_by_isbn(left, right)


def merge_by_isbn(left, right):
    """
    Merge two sorted lists by ISBN (ascending).
    
    Args:
        left (list): First sorted list
        right (list): Second sorted list
    
    Returns:
        list: Merged sorted list
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i].isbn <= right[j].isbn:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# Testing module
if __name__ == "__main__":
    import sys
    sys.path.append('../..')
    from src.models.book import Book
    
    # Create test books
    books = [
        Book("978-3", "Book C", "Author 3", 1.0, 50000, 2),
        Book("978-1", "Book A", "Author 1", 0.8, 100000, 3),
        Book("978-2", "Book B", "Author 2", 1.2, 75000, 1),
    ]
    
    print("=== Testing Sorting Algorithms ===\n")
    print("Original list:")
    for book in books:
        print(f"  {book.isbn} - {book.title} - ${book.value}")
    
    # Test Insertion Sort by ISBN
    sorted_isbn = books.copy()
    insertion_sort_by_isbn(sorted_isbn)
    print("\nAfter Insertion Sort (by ISBN):")
    for book in sorted_isbn:
        print(f"  {book.isbn} - {book.title}")
    
    # Test Merge Sort by Value
    sorted_value = merge_sort_by_value(books.copy())
    print("\nAfter Merge Sort (by Value - descending):")
    for book in sorted_value:
        print(f"  ${book.value} - {book.title}")
