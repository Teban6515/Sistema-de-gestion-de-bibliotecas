"""Loan Manager - Manages book loans and returns with Stack structure"""
from ..data_structures.stack import Stack
from datetime import datetime

class LoanManager:
    """
    GESTIÓN DE PRÉSTAMOS DE LIBROS

    Administra el historial de préstamos usando una estructura Stack (pila) para cada usuario.
    Stack permite acceso LIFO (Last In, First Out) - el préstamo más reciente está al tope.
    """
    def __init__(self, inventory_manager):
        # Dict: user_id -> Stack con historial de préstamos de ese usuario
        self.loan_histories = {}
        # Referencia al gestor de inventario para verificar disponibilidad y actualizar stock
        self.inventory_manager = inventory_manager

    def loan_book(self, user_id, isbn):
        """
        PRESTAR UN LIBRO A UN USUARIO

        Proceso:
        1. Verifica disponibilidad del libro (stock > 0)
        2. Decrementa el stock del libro
        3. Crea registro con ISBN, título, fecha y estado
        4. Agrega registro al Stack del usuario

        Retorna: (True/False, mensaje)
        """
        # Si el usuario no tiene historial, crea un Stack vacío
        if user_id not in self.loan_histories:
            self.loan_histories[user_id] = Stack()

        # Busca el libro por ISBN en el inventario ordenado (búsqueda binaria)
        book = self.inventory_manager.search_by_isbn(isbn)
        if not book or not book.is_available():
            return False, "Book not available"

        # Decrementa el stock del libro (book.stock -= 1)
        book.decrease_stock()

        # Crea el registro del préstamo con fecha ISO actual
        loan_record = {
            'isbn': isbn,
            'title': book.title,
            'loan_date': datetime.now().isoformat(),  # Formato: 2025-12-11T10:30:45
            'returned': False  # Estado inicial: NO devuelto
        }

        # Agrega el registro al tope del Stack del usuario (push)
        self.loan_histories[user_id].push(loan_record)
        return True, f"Book loaned: {book.title}"
    
    def return_book(self, user_id, isbn):
        """
        DEVOLVER UN LIBRO

        Proceso:
        1. Verifica que el usuario tenga historial de préstamos
        2. Incrementa el stock del libro
        3. Busca el préstamo activo (returned=False) en el Stack del usuario
        4. Marca el registro como devuelto y registra fecha de devolución

        Retorna: (True/False, mensaje)
        """
        # Verifica que el usuario exista y tenga préstamos
        if user_id not in self.loan_histories or self.loan_histories[user_id].is_empty():
            return False, "No loan history found"

        # Busca el libro por ISBN
        book = self.inventory_manager.search_by_isbn(isbn)
        if not book:
            return False, "Book not found"

        # Incrementa el stock del libro (book.stock += 1)
        book.increase_stock()

        # Busca el préstamo activo en el Stack del usuario
        for loan in self.loan_histories[user_id].items:
            # Solo considera préstamos NO devueltos del mismo ISBN
            if loan['isbn'] == isbn and not loan.get('returned', False):
                loan['returned'] = True  # Marca como devuelto
                loan['return_date'] = datetime.now().isoformat()  # Registra fecha
                return True, f"Book returned: {book.title}"

        return False, "Loan record not found"
    
    def get_user_history(self, user_id):
        """
        OBTENER HISTORIAL DE PRÉSTAMOS DE UN USUARIO

        Retorna el Stack completo con todos los préstamos (activos y devueltos).
        Si el usuario no tiene historial, retorna un Stack vacío.
        """
        return self.loan_histories.get(user_id, Stack())
