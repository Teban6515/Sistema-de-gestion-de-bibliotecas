"""
Validators Utility

This module provides validation functions for user input and data integrity.

Author: Miguel Bravo
Date: December 2025
Course: Programming Techniques
"""

import re


def validate_isbn(isbn):
    """
    Validate ISBN format.
    
    Accepts ISBN-10 or ISBN-13 formats.
    
    Args:
        isbn (str): ISBN to validate
    
    Returns:
        tuple: (is_valid, error_message)
    
    Examples:
        >>> validate_isbn("978-0-13-468599-1")
        (True, None)
        >>> validate_isbn("123")
        (False, "ISBN must be at least 10 characters")
    """
    if not isbn or not isinstance(isbn, str):
        return (False, "ISBN must be a non-empty string")
    
    # Remove hyphens and spaces
    clean_isbn = isbn.replace('-', '').replace(' ', '')
    
    # Check length
    if len(clean_isbn) < 10:
        return (False, "ISBN must be at least 10 characters")
    
    if len(clean_isbn) > 13:
        return (False, "ISBN must not exceed 13 characters")
    
    # Check if all characters are digits or X (for ISBN-10)
    if not (clean_isbn[:-1].isdigit() and (clean_isbn[-1].isdigit() or clean_isbn[-1].upper() == 'X')):
        return (False, "ISBN must contain only digits (and optionally 'X' at the end)")
    
    return (True, None)


def validate_email(email):
    """
    Validate email address format.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        tuple: (is_valid, error_message)
    
    Examples:
        >>> validate_email("user@example.com")
        (True, None)
        >>> validate_email("invalid-email")
        (False, "Email must contain '@' and a domain")
    """
    if not email or not isinstance(email, str):
        return (False, "Email must be a non-empty string")
    
    # Basic email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, email):
        return (False, "Invalid email format (expected: user@domain.com)")
    
    return (True, None)


def validate_phone(phone):
    """
    Validate phone number format.
    
    Accepts Colombian phone numbers with optional country code.
    
    Args:
        phone (str): Phone number to validate
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not phone:
        return (True, None)  # Phone is optional
    
    if not isinstance(phone, str):
        return (False, "Phone must be a string")
    
    # Remove spaces, hyphens, parentheses
    clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
    
    # Check if starts with + (country code)
    if clean_phone.startswith('+'):
        if len(clean_phone) < 10:
            return (False, "Phone number too short")
        if not clean_phone[1:].isdigit():
            return (False, "Phone must contain only digits after +")
    else:
        if len(clean_phone) < 7:
            return (False, "Phone number too short")
        if not clean_phone.isdigit():
            return (False, "Phone must contain only digits")
    
    return (True, None)


def validate_weight(weight):
    """
    Validate book weight.
    
    Args:
        weight (float): Weight in kilograms
    
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        weight_float = float(weight)
        
        if weight_float <= 0:
            return (False, "Weight must be positive")
        
        if weight_float > 50:
            return (False, "Weight seems unrealistic for a book (max 50 Kg)")
        
        return (True, None)
    except (ValueError, TypeError):
        return (False, "Weight must be a valid number")


def validate_value(value):
    """
    Validate book value (price in COP).
    
    Args:
        value (int/float): Value in Colombian pesos
    
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        value_int = int(value)
        
        if value_int < 0:
            return (False, "Value cannot be negative")
        
        if value_int > 10_000_000:
            return (False, "Value seems unrealistic for a book (max $10,000,000 COP)")
        
        return (True, None)
    except (ValueError, TypeError):
        return (False, "Value must be a valid number")


def validate_stock(stock):
    """
    Validate stock quantity.
    
    Args:
        stock (int): Number of copies
    
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        stock_int = int(stock)
        
        if stock_int < 0:
            return (False, "Stock cannot be negative")
        
        if stock_int > 1000:
            return (False, "Stock seems unrealistic (max 1000 copies)")
        
        return (True, None)
    except (ValueError, TypeError):
        return (False, "Stock must be a valid integer")


def validate_user_id(user_id):
    """
    Validate user ID format.
    
    Args:
        user_id (str): User ID to validate
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not user_id or not isinstance(user_id, str):
        return (False, "User ID must be a non-empty string")
    
    if len(user_id) < 3:
        return (False, "User ID must be at least 3 characters")
    
    if len(user_id) > 20:
        return (False, "User ID must not exceed 20 characters")
    
    # Allow alphanumeric and underscore
    if not re.match(r'^[a-zA-Z0-9_]+$', user_id):
        return (False, "User ID must contain only letters, numbers, and underscores")
    
    return (True, None)


def validate_name(name):
    """
    Validate person's name.
    
    Args:
        name (str): Name to validate
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not name or not isinstance(name, str):
        return (False, "Name must be a non-empty string")
    
    if len(name) < 2:
        return (False, "Name must be at least 2 characters")
    
    if len(name) > 100:
        return (False, "Name must not exceed 100 characters")
    
    # Allow letters, spaces, hyphens, apostrophes
    if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\-']+$", name):
        return (False, "Name contains invalid characters")
    
    return (True, None)


def sanitize_input(text, max_length=None):
    """
    Sanitize user input by removing dangerous characters.
    
    Args:
        text (str): Input text to sanitize
        max_length (int, optional): Maximum allowed length
    
    Returns:
        str: Sanitized text
    """
    if not isinstance(text, str):
        return str(text)
    
    # Remove leading/trailing whitespace
    sanitized = text.strip()
    
    # Limit length if specified
    if max_length and len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    return sanitized


def validate_date_format(date_str):
    """
    Validate date format (YYYY-MM-DD or ISO format).
    
    Args:
        date_str (str): Date string to validate
    
    Returns:
        tuple: (is_valid, error_message)
    """
    from datetime import datetime
    
    if not date_str or not isinstance(date_str, str):
        return (False, "Date must be a non-empty string")
    
    # Try parsing with common formats
    formats = ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%S.%f']
    
    for fmt in formats:
        try:
            datetime.strptime(date_str.split('+')[0].split('Z')[0], fmt)
            return (True, None)
        except ValueError:
            continue
    
    return (False, "Invalid date format (expected: YYYY-MM-DD or ISO format)")


def validate_max_loans(max_loans):
    """
    Validate maximum number of simultaneous loans.
    
    Args:
        max_loans (int): Maximum loans allowed
    
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        max_int = int(max_loans)
        
        if max_int < 1:
            return (False, "Maximum loans must be at least 1")
        
        if max_int > 20:
            return (False, "Maximum loans seems unrealistic (max 20)")
        
        return (True, None)
    except (ValueError, TypeError):
        return (False, "Maximum loans must be a valid integer")


# Testing module
if __name__ == "__main__":
    print("=== Testing Validators ===\n")
    
    # Test ISBN validation
    test_isbns = [
        "978-0-13-468599-1",
        "123",
        "978-0-13-ABCD-1",
        "0-306-40615-2"
    ]
    
    print("ISBN Validation:")
    for isbn in test_isbns:
        valid, error = validate_isbn(isbn)
        status = "✅" if valid else "❌"
        print(f"  {status} '{isbn}': {error or 'Valid'}")
    
    # Test email validation
    test_emails = [
        "user@example.com",
        "invalid-email",
        "test@domain.co.uk",
        "@invalid.com"
    ]
    
    print("\nEmail Validation:")
    for email in test_emails:
        valid, error = validate_email(email)
        status = "✅" if valid else "❌"
        print(f"  {status} '{email}': {error or 'Valid'}")
    
    # Test weight validation
    test_weights = [1.5, 0, -1, 100]
    
    print("\nWeight Validation:")
    for weight in test_weights:
        valid, error = validate_weight(weight)
        status = "✅" if valid else "❌"
        print(f"  {status} {weight} Kg: {error or 'Valid'}")
