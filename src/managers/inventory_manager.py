"""Inventory Manager - Manages both general and sorted inventories"""
from ..algorithms.sorting import insertion_sort_by_isbn, merge_sort_by_value
from ..algorithms.searching import binary_search_by_isbn, linear_search_by_title, linear_search_by_author

class InventoryManager:
    def __init__(self):
        self.general_inventory = []
        self.sorted_inventory = []
    
    def add_book(self, book):
        self.general_inventory.append(book)
        self.sorted_inventory.append(book)
        insertion_sort_by_isbn(self.sorted_inventory)
        return True
    
    def remove_book(self, isbn):
        idx = binary_search_by_isbn(self.sorted_inventory, isbn)
        if idx != -1:
            book = self.sorted_inventory[idx]
            self.sorted_inventory.pop(idx)
            self.general_inventory.remove(book)
            return book
        return None
    
    def search_by_isbn(self, isbn):
        idx = binary_search_by_isbn(self.sorted_inventory, isbn)
        return self.sorted_inventory[idx] if idx != -1 else None
    
    def search_by_title(self, title):
        return linear_search_by_title(self.general_inventory, title)
    
    def search_by_author(self, author):
        return linear_search_by_author(self.general_inventory, author)
    
    def generate_value_report(self):
        return merge_sort_by_value(self.general_inventory.copy())
    
    def get_all_books(self):
        return self.general_inventory.copy()
    
    def get_sorted_books(self):
        return self.sorted_inventory.copy()
