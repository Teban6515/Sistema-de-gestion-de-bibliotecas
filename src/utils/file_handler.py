"""
File Handler Utility

This module provides functions for loading and saving data to/from JSON files.
Handles all file I/O operations for the Library Management System.

Author: Miguel Bravo
Date: December 2025
Course: Programming Techniques
"""

import json
import os
from datetime import datetime


def load_books(filename='data/books.json'):
    """
    Load books from JSON file.
    
    Args:
        filename (str): Path to books JSON file
    
    Returns:
        list: List of Book objects
    
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    from ..models.book import Book
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            books = [Book.from_dict(book_data) for book_data in data['books']]
            print(f"✅ Loaded {len(books)} books from {filename}")
            return books
    except FileNotFoundError:
        print(f"⚠️  File not found: {filename}")
        print(f"Creating empty books list...")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Error reading JSON file: {e}")
        return []
    except Exception as e:
        print(f"❌ Unexpected error loading books: {e}")
        return []


def save_books(books, filename='data/books.json'):
    """
    Save books to JSON file.
    
    Args:
        books (list): List of Book objects
        filename (str): Path to output JSON file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        data = {
            'books': [book.to_dict() for book in books],
            'last_updated': datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved {len(books)} books to {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving books: {e}")
        return False


def load_users(filename='data/users.json'):
    """
    Load users from JSON file.
    
    Args:
        filename (str): Path to users JSON file
    
    Returns:
        dict: Dictionary mapping user_id to User objects
    """
    from ..models.user import User
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            users = {user_data['user_id']: User.from_dict(user_data) 
                    for user_data in data['users']}
            print(f"✅ Loaded {len(users)} users from {filename}")
            return users
    except FileNotFoundError:
        print(f"⚠️  File not found: {filename}")
        return {}
    except Exception as e:
        print(f"❌ Error loading users: {e}")
        return {}


def save_users(users, filename='data/users.json'):
    """
    Save users to JSON file.
    
    Args:
        users (dict): Dictionary of user_id -> User objects
        filename (str): Path to output JSON file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        data = {
            'users': [user.to_dict() for user in users.values()],
            'last_updated': datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved {len(users)} users to {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving users: {e}")
        return False


def load_loan_history(filename='data/loans_history.json'):
    """
    Load loan history from JSON file.
    
    Args:
        filename (str): Path to loan history JSON file
    
    Returns:
        dict: Dictionary mapping user_id to Stack of loan records
    """
    from ..data_structures.stack import Stack
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            loan_histories = {}
            for user_id, history_data in data.get('loan_history', {}).items():
                stack = Stack()
                stack.items = history_data.get('history', [])
                loan_histories[user_id] = stack
            
            print(f"✅ Loaded loan history for {len(loan_histories)} users from {filename}")
            return loan_histories
    except FileNotFoundError:
        print(f"⚠️  File not found: {filename}")
        return {}
    except Exception as e:
        print(f"❌ Error loading loan history: {e}")
        return {}


def save_loan_history(loan_histories, filename='data/loans_history.json'):
    """
    Save loan history to JSON file.
    
    Args:
        loan_histories (dict): Dictionary of user_id -> Stack
        filename (str): Path to output JSON file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        data = {
            'loan_history': {
                user_id: {'user_id': user_id, 'history': stack.items}
                for user_id, stack in loan_histories.items()
            },
            'last_updated': datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved loan history for {len(loan_histories)} users to {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving loan history: {e}")
        return False


def load_reservations(filename='data/reservations.json'):
    """
    Load book reservations from JSON file.
    
    Args:
        filename (str): Path to reservations JSON file
    
    Returns:
        dict: Dictionary mapping ISBN to Queue of reservations
    """
    from ..data_structures.queue import Queue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            reservations = {}
            for isbn, reservation_data in data.get('reservations', {}).items():
                queue = Queue()
                queue.items = reservation_data.get('queue', [])
                reservations[isbn] = queue
            
            print(f"✅ Loaded reservations for {len(reservations)} books from {filename}")
            return reservations
    except FileNotFoundError:
        print(f"⚠️  File not found: {filename}")
        return {}
    except Exception as e:
        print(f"❌ Error loading reservations: {e}")
        return {}


def save_reservations(reservations, filename='data/reservations.json'):
    """
    Save book reservations to JSON file.
    
    Args:
        reservations (dict): Dictionary of ISBN -> Queue
        filename (str): Path to output JSON file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        data = {
            'reservations': {
                isbn: {'isbn': isbn, 'queue': queue.items}
                for isbn, queue in reservations.items()
            },
            'last_updated': datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved reservations for {len(reservations)} books to {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving reservations: {e}")
        return False


def backup_data(backup_dir='data/backups'):
    """
    Create backup copies of all data files.
    
    Args:
        backup_dir (str): Directory for backup files
    
    Returns:
        bool: True if successful, False otherwise
    """
    import shutil
    
    try:
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        files_to_backup = [
            'data/books.json',
            'data/users.json',
            'data/loans_history.json',
            'data/reservations.json'
        ]
        
        for file_path in files_to_backup:
            if os.path.exists(file_path):
                filename = os.path.basename(file_path)
                backup_path = os.path.join(backup_dir, f"{timestamp}_{filename}")
                shutil.copy2(file_path, backup_path)
                print(f"✅ Backed up: {file_path} -> {backup_path}")
        
        return True
    except Exception as e:
        print(f"❌ Error creating backup: {e}")
        return False


# Testing module
if __name__ == "__main__":
    print("=== Testing File Handler ===\n")
    
    # Test loading books
    books = load_books()
    if books:
        print(f"\nFirst book: {books[0]}")
        print(f"Last book: {books[-1]}")
    
    # Test loading users
    users = load_users()
    if users:
        print(f"\nFirst user: {list(users.values())[0]}")
    
    # Test backup
    print("\nCreating backup...")
    backup_data()
