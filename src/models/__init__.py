"""
Models Package

This package contains the core data models for the Library Management System.

Classes:
    - Book: Represents a book in the inventory
    - User: Represents a library user
    - Shelf: Represents a physical shelf

Author: [Your Name]
Date: December 2025
"""

from .book import Book
from .user import User
from .shelf import Shelf

__all__ = ['Book', 'User', 'Shelf']
