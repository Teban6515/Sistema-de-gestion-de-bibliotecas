"""
Data Structures Package

This package contains custom implementations of fundamental data structures
for the Library Management System.

Classes:
    - Stack: LIFO (Last In, First Out) structure for loan history
    - Queue: FIFO (First In, First Out) structure for reservations

Author: [Your Name]
Date: December 2025
"""

from .stack import Stack
from .queue import Queue

__all__ = ['Stack', 'Queue']
