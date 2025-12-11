"""Loan Manager - Manages book loans and returns with Stack structure"""
from ..data_structures.stack import Stack
from datetime import datetime

class LoanManager:
    def __init__(self, inventory_manager):
        self.loan_histories = {}
        self.inventory_manager = inventory_manager
    
    def loan_book(self, user_id, isbn):
        if user_id not in self.loan_histories:
            self.loan_histories[user_id] = Stack()
        
        book = self.inventory_manager.search_by_isbn(isbn)
        if not book or not book.is_available():
            return False, "Book not available"
        
        book.decrease_stock()
        loan_record = {
            'isbn': isbn,
            'title': book.title,
            'loan_date': datetime.now().isoformat(),
            'returned': False
        }
        self.loan_histories[user_id].push(loan_record)
        return True, f"Book loaned: {book.title}"
    
    def return_book(self, user_id, isbn):
        if user_id not in self.loan_histories or self.loan_histories[user_id].is_empty():
            return False, "No loan history found"
        
        book = self.inventory_manager.search_by_isbn(isbn)
        if not book:
            return False, "Book not found"
        
        book.increase_stock()
        
        for loan in self.loan_histories[user_id].items:
            if loan['isbn'] == isbn and not loan.get('returned', False):
                loan['returned'] = True
                loan['return_date'] = datetime.now().isoformat()
                return True, f"Book returned: {book.title}"
        
        return False, "Loan record not found"
    
    def get_user_history(self, user_id):
        return self.loan_histories.get(user_id, Stack())
