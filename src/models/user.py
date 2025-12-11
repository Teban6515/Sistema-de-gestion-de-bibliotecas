"""
User Model

This module defines the User class which represents a library user.
Each user has personal information and a loan history managed as a Stack.

Author: [Your Name]
Date: December 2025
Course: Programming Techniques
"""

from datetime import datetime

class User:
    """
    Represents a library user with loan history.
    
    Attributes:
        user_id (str): Unique user identifier
        name (str): User's full name
        email (str): User's email address
        phone (str): User's phone number
        address (str): User's address
        registration_date (str): Date when user registered
        active (bool): Whether the user account is active
        max_loans (int): Maximum number of simultaneous loans allowed
    
    Methods:
        to_dict(): Convert user object to dictionary
        from_dict(data): Create user object from dictionary
        can_borrow(): Check if user can borrow more books
        __str__(): String representation
        __repr__(): Developer representation
        __eq__(): Compare users by ID
    """
    
    def __init__(self, user_id, name, email, phone="", address="", 
                 registration_date=None, active=True, max_loans=5):
        """
        Initialize a new User object.
        
        Args:
            user_id (str): Unique identifier for the user
            name (str): User's full name
            email (str): User's email address
            phone (str, optional): Phone number. Defaults to "".
            address (str, optional): Physical address. Defaults to "".
            registration_date (str, optional): Registration date. Defaults to today.
            active (bool, optional): Account status. Defaults to True.
            max_loans (int, optional): Max simultaneous loans. Defaults to 5.
        
        Raises:
            ValueError: If required parameters are invalid
        """
        # Validation
        if not user_id or not isinstance(user_id, str):
            raise ValueError("User ID must be a non-empty string")
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a non-empty string")
        if '@' not in email:
            raise ValueError("Email must contain @")
        if max_loans < 1:
            raise ValueError("Max loans must be at least 1")
        
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.registration_date = registration_date or datetime.now().strftime("%Y-%m-%d")
        self.active = active
        self.max_loans = max_loans  # Límite de préstamos simultáneos (default: 5)
        self.current_loans = 0  # Contador de préstamos activos (se incrementa/decrementa al prestar/devolver)
    
    def can_borrow(self):
        """
        VERIFICAR SI EL USUARIO PUEDE PRESTAR MÁS LIBROS

        Usado en main.py -> _loan_book() antes de permitir préstamos.
        Verifica que el usuario esté activo y no haya alcanzado el límite.

        Returns:
            bool: True si puede prestar (active=True y current_loans < max_loans)
        """
        return self.active and self.current_loans < self.max_loans
    
    def increment_loans(self):
        """
        INCREMENTAR CONTADOR DE PRÉSTAMOS ACTIVOS

        Se llama en main.py -> _loan_book() después de un préstamo exitoso.
        Incrementa current_loans en 1.

        Returns:
            bool: True si exitoso, False si está en el límite máximo
        """
        if self.can_borrow():
            self.current_loans += 1
            return True
        return False
    
    def decrement_loans(self):
        """
        DECREMENTAR CONTADOR DE PRÉSTAMOS ACTIVOS

        Se llama en main.py -> _return_book() después de una devolución exitosa.
        Decrementa current_loans en 1.

        Returns:
            bool: True si exitoso, False si no tiene préstamos activos
        """
        if self.current_loans > 0:
            self.current_loans -= 1
            return True
        return False
    
    def deactivate(self):
        """
        Deactivate the user account.
        """
        self.active = False
    
    def activate(self):
        """
        Activate the user account.
        """
        self.active = True
    
    def to_dict(self):
        """
        Convert user object to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the user
        """
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'registration_date': self.registration_date,
            'active': self.active,
            'max_loans': self.max_loans,
            'current_loans': self.current_loans
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a User object from a dictionary.
        
        Args:
            data (dict): Dictionary containing user data
        
        Returns:
            User: New User object created from dictionary
        
        Raises:
            KeyError: If required keys are missing
        """
        user = User(
            user_id=data['user_id'],
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', ''),
            address=data.get('address', ''),
            registration_date=data.get('registration_date'),
            active=data.get('active', True),
            max_loans=data.get('max_loans', 5)
        )
        user.current_loans = data.get('current_loans', 0)
        return user
    
    def __str__(self):
        """
        String representation for end users.
        
        Returns:
            str: Formatted string with user information
        """
        status = "✅ Active" if self.active else "❌ Inactive"
        return (f"👤 {self.name}\n"
                f"   ID: {self.user_id}\n"
                f"   Email: {self.email}\n"
                f"   Status: {status}\n"
                f"   Current Loans: {self.current_loans}/{self.max_loans}")
    
    def __repr__(self):
        """
        Developer-friendly representation.
        
        Returns:
            str: Technical representation of the user
        """
        return f"User(user_id='{self.user_id}', name='{self.name}', loans={self.current_loans})"
    
    def __eq__(self, other):
        """
        Compare two users for equality based on user_id.
        
        Args:
            other (User): Another user object
        
        Returns:
            bool: True if user_ids are equal
        """
        if not isinstance(other, User):
            return False
        return self.user_id == other.user_id
    
    def __hash__(self):
        """
        Make User hashable for use in sets and as dict keys.
        
        Returns:
            int: Hash value based on user_id
        """
        return hash(self.user_id)


# Example usage and testing
if __name__ == "__main__":
    # Create a test user
    user1 = User(
        user_id="U001",
        name="Miguel Bravo",
        email="miguel.bravo@ucaldas.edu.co",
        phone="+57 300 1234567",
        address="Manizales, Caldas",
        max_loans=3
    )
    
    print(user1)
    print(f"\nCan borrow? {user1.can_borrow()}")
    
    # Simulate borrowing books
    user1.increment_loans()
    user1.increment_loans()
    print(f"\nAfter borrowing 2 books:")
    print(user1)
    
    # Test dictionary conversion
    user_dict = user1.to_dict()
    print(f"\nDictionary: {user_dict}")
    
    # Test creating from dictionary
    user2 = User.from_dict(user_dict)
    print(f"\nRecreated: {user2}")
    
    # Test comparison
    print(f"\nAre they equal? {user1 == user2}")
