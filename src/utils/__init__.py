"""
Utilities Package

This package contains utility functions for file handling and validation.

Modules:
    - file_handler: Load and save JSON data files
    - validators: Validate user input and data integrity

Author: Miguel Bravo
Date: December 2025
"""

from .file_handler import (
    load_books,
    save_books,
    load_users,
    save_users,
    load_loan_history,
    save_loan_history,
    load_reservations,
    save_reservations,
    backup_data
)

from .validators import (
    validate_isbn,
    validate_email,
    validate_phone,
    validate_weight,
    validate_value,
    validate_stock,
    validate_user_id,
    validate_name,
    validate_date_format,
    validate_max_loans,
    sanitize_input
)

__all__ = [
    # File Handler
    'load_books',
    'save_books',
    'load_users',
    'save_users',
    'load_loan_history',
    'save_loan_history',
    'load_reservations',
    'save_reservations',
    'backup_data',
    # Validators
    'validate_isbn',
    'validate_email',
    'validate_phone',
    'validate_weight',
    'validate_value',
    'validate_stock',
    'validate_user_id',
    'validate_name',
    'validate_date_format',
    'validate_max_loans',
    'sanitize_input',
]
