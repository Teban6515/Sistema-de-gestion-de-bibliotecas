"""
Algorithms Package

This package contains all algorithm implementations for the Library Management System.

Modules:
    - sorting: Insertion Sort and Merge Sort algorithms
    - searching: Linear Search and Binary Search algorithms
    - recursion: Stack recursion and tail recursion functions

Author: [Teban y Migue]
Date: December 2025
"""

from .sorting import (
    insertion_sort_by_isbn,
    insertion_sort_by_value,
    merge_sort_by_value,
    merge_sort_by_isbn
)

from .searching import (
    linear_search_by_title,
    linear_search_by_author,
    linear_search_by_isbn,
    binary_search_by_isbn,
    binary_search_recursive,
    verify_book_has_reservations
)

from .recursion import (
    calculate_total_value_by_author,
    calculate_average_weight_by_author,
    demonstrate_tail_recursion_conversion
)

__all__ = [
    # Sorting
    'insertion_sort_by_isbn',
    'insertion_sort_by_value',
    'merge_sort_by_value',
    'merge_sort_by_isbn',
    # Searching
    'linear_search_by_title',
    'linear_search_by_author',
    'linear_search_by_isbn',
    'binary_search_by_isbn',
    'binary_search_recursive',
    'verify_book_has_reservations',
    # Recursion
    'calculate_total_value_by_author',
    'calculate_average_weight_by_author',
    'demonstrate_tail_recursion_conversion',
]
