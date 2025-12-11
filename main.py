"""
Library Management System - Main Application

This is the main entry point for the Library Management System.
Provides an interactive menu for all system operations.

Author: Miguel Bravo
Date: December 2025
Course: Programming Techniques - Universidad de Caldas
"""

import os
import sys
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.models.book import Book
from src.models.user import User
from src.managers.inventory_manager import InventoryManager
from src.managers.loan_manager import LoanManager
from src.managers.user_manager import UserManager
from src.utils.file_handler import (
    load_books, save_books,
    load_users, save_users,
    load_loan_history, save_loan_history,
    load_reservations, save_reservations,
    backup_data
)
from src.utils.validators import *
from src.algorithms.recursion import (
    calculate_total_value_by_author,
    calculate_average_weight_by_author
)
from src.problem_solving.brute_force import (
    find_risky_shelf_combinations,
    display_risky_combinations,
    generate_risky_combinations_report
)
from src.problem_solving.backtracking import (
    find_optimal_shelf_backtracking,
    display_optimal_solution,
    generate_optimal_shelf_report
)


class LibraryManagementSystem:
    """Main system class integrating all managers"""
    
    def __init__(self):
        print("\n" + "="*80)
        print(" "*25 + "LIBRARY MANAGEMENT SYSTEM")
        print(" "*20 + "Universidad de Caldas - 2025")
        print("="*80)
        print("\nLoading system...")
        
        # Initialize managers
        self.inventory = InventoryManager()
        self.loan_manager = LoanManager(self.inventory)
        self.user_manager = UserManager()
        
        # Load data
        self._load_all_data()
        
        print(f"\n✅ System ready!")
        print(f"   📚 Books: {len(self.inventory.general_inventory)}")
        print(f"   👤 Users: {len(self.user_manager.users)}")
    
    def _load_all_data(self):
        """Load all data from files"""
        # Load books
        books = load_books()
        for book in books:
            self.inventory.general_inventory.append(book)
            self.inventory.sorted_inventory.append(book)
        from src.algorithms.sorting import insertion_sort_by_isbn
        insertion_sort_by_isbn(self.inventory.sorted_inventory)
        
        # Load users
        users_dict = load_users()
        self.user_manager.users = users_dict
        
        # Load loan history
        self.loan_manager.loan_histories = load_loan_history()
    
    def _save_all_data(self):
        """Save all data to files"""
        save_books(self.inventory.general_inventory)
        save_users(self.user_manager.users)
        save_loan_history(self.loan_manager.loan_histories)
        print("\n✅ All data saved successfully!")
    
    def run(self):
        """Main application loop"""
        while True:
            self._show_main_menu()
            choice = input("\n👉 Select option: ").strip()
            
            if choice == '1':
                self._book_management_menu()
            elif choice == '2':
                self._user_management_menu()
            elif choice == '3':
                self._loan_management_menu()
            elif choice == '4':
                self._shelf_analysis_menu()
            elif choice == '5':
                self._recursive_functions_menu()
            elif choice == '6':
                self._generate_reports_menu()
            elif choice == '7':
                self._save_all_data()
            elif choice == '8':
                backup_data()
            elif choice == '9':
                self._save_all_data()
                print("\n👋 Thank you for using the Library Management System!")
                print("   Developed by: Miguel Bravo - Universidad de Caldas")
                break
            else:
                print("\n❌ Invalid option. Please try again.")
            
            input("\nPress Enter to continue...")
    
    def _show_main_menu(self):
        """Display main menu"""
        print("\n" + "="*80)
        print(" "*30 + "MAIN MENU")
        print("="*80)
        print("\n📚 BOOK MANAGEMENT")
        print("   1. Book Operations (Add, Search, Update, Delete, List)")
        print("\n👤 USER MANAGEMENT")
        print("   2. User Operations (Add, Search, Update, Delete, List)")
        print("\n📖 LOAN MANAGEMENT")
        print("   3. Loan Operations (Loan Book, Return Book, View History)")
        print("\n🔬 ALGORITHMS & ANALYSIS")
        print("   4. Shelf Analysis (Brute Force & Backtracking)")
        print("   5. Recursive Functions (Stack & Tail Recursion)")
        print("   6. Generate Reports (Sorted by Value)")
        print("\n💾 SYSTEM")
        print("   7. Save All Data")
        print("   8. Create Backup")
        print("   9. Exit")
        print("="*80)
    
    # ========================================================================
    # BOOK MANAGEMENT
    # ========================================================================
    
    def _book_management_menu(self):
        """Book management submenu"""
        while True:
            print("\n" + "-"*80)
            print(" "*30 + "BOOK MANAGEMENT")
            print("-"*80)
            print("1. Add New Book")
            print("2. Search Book")
            print("3. List All Books")
            print("4. Update Book")
            print("5. Delete Book")
            print("6. Back to Main Menu")
            
            choice = input("\n👉 Select option: ").strip()
            
            if choice == '1':
                self._add_book()
            elif choice == '2':
                self._search_book()
            elif choice == '3':
                self._list_books()
            elif choice == '4':
                self._update_book()
            elif choice == '5':
                self._delete_book()
            elif choice == '6':
                break
    
    def _add_book(self):
        """Add a new book"""
        print("\n📚 ADD NEW BOOK")
        print("-"*80)
        
        # Get and validate ISBN
        isbn = input("ISBN: ").strip()
        valid, error = validate_isbn(isbn)
        if not valid:
            print(f"❌ {error}")
            return
        
        # Check if ISBN already exists
        if self.inventory.search_by_isbn(isbn):
            print(f"❌ Book with ISBN {isbn} already exists!")
            return
        
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        
        weight = input("Weight (Kg): ").strip()
        valid, error = validate_weight(weight)
        if not valid:
            print(f"❌ {error}")
            return
        
        value = input("Value (COP): ").strip()
        valid, error = validate_value(value)
        if not valid:
            print(f"❌ {error}")
            return
        
        stock = input("Stock (default 1): ").strip() or "1"
        valid, error = validate_stock(stock)
        if not valid:
            print(f"❌ {error}")
            return
        
        category = input("Category (optional): ").strip() or "General"
        publisher = input("Publisher (optional): ").strip() or "Unknown"
        year = input("Year (optional): ").strip() or str(datetime.now().year)
        
        try:
            book = Book(isbn, title, author, float(weight), int(value), 
                       int(stock), category, publisher, int(year))
            self.inventory.add_book(book)
            print(f"\n✅ Book added successfully!")
            print(book)
        except Exception as e:
            print(f"\n❌ Error adding book: {e}")
    
    def _search_book(self):
        """Search for books"""
        print("\n🔍 SEARCH BOOK")
        print("-"*80)
        print("1. Search by ISBN")
        print("2. Search by Title")
        print("3. Search by Author")
        
        choice = input("\n👉 Select search type: ").strip()
        
        if choice == '1':
            isbn = input("Enter ISBN: ").strip()
            book = self.inventory.search_by_isbn(isbn)
            if book:
                print("\n✅ Book found:")
                print(book)
            else:
                print("\n❌ Book not found")
        
        elif choice == '2':
            title = input("Enter title (partial match): ").strip()
            books = self.inventory.search_by_title(title)
            if books:
                print(f"\n✅ Found {len(books)} book(s):")
                for i, book in enumerate(books, 1):
                    print(f"\n[{i}]")
                    print(book)
            else:
                print("\n❌ No books found")
        
        elif choice == '3':
            author = input("Enter author (partial match): ").strip()
            books = self.inventory.search_by_author(author)
            if books:
                print(f"\n✅ Found {len(books)} book(s):")
                for i, book in enumerate(books, 1):
                    print(f"\n[{i}]")
                    print(book)
            else:
                print("\n❌ No books found")
    
    def _list_books(self):
        """List all books"""
        books = self.inventory.get_all_books()
        if not books:
            print("\n📚 No books in inventory")
            return
        
        print(f"\n📚 INVENTORY ({len(books)} books)")
        print("-"*80)
        for i, book in enumerate(books, 1):
            print(f"\n[{i}]")
            print(book)
    
    def _update_book(self):
        """Update book information"""
        isbn = input("\nEnter ISBN of book to update: ").strip()
        book = self.inventory.search_by_isbn(isbn)
        
        if not book:
            print("❌ Book not found")
            return
        
        print(f"\nCurrent information:")
        print(book)
        print("\nEnter new values (press Enter to keep current):")
        
        new_stock = input(f"Stock ({book.stock}): ").strip()
        if new_stock:
            valid, error = validate_stock(new_stock)
            if valid:
                book.stock = int(new_stock)
        
        print("\n✅ Book updated successfully!")
    
    def _delete_book(self):
        """Delete a book"""
        isbn = input("\nEnter ISBN of book to delete: ").strip()
        book = self.inventory.remove_book(isbn)
        
        if book:
            print(f"\n✅ Book deleted: {book.title}")
        else:
            print("\n❌ Book not found")
    
    # ========================================================================
    # USER MANAGEMENT
    # ========================================================================
    
    def _user_management_menu(self):
        """User management submenu"""
        while True:
            print("\n" + "-"*80)
            print(" "*30 + "USER MANAGEMENT")
            print("-"*80)
            print("1. Add New User")
            print("2. Search User")
            print("3. List All Users")
            print("4. Update User")
            print("5. Delete User")
            print("6. Back to Main Menu")
            
            choice = input("\n👉 Select option: ").strip()
            
            if choice == '1':
                self._add_user()
            elif choice == '2':
                self._search_user()
            elif choice == '3':
                self._list_users()
            elif choice == '4':
                self._update_user()
            elif choice == '5':
                self._delete_user()
            elif choice == '6':
                break
    
    def _add_user(self):
        """Add a new user"""
        print("\n👤 ADD NEW USER")
        print("-"*80)
        
        user_id = input("User ID: ").strip()
        valid, error = validate_user_id(user_id)
        if not valid:
            print(f"❌ {error}")
            return
        
        if self.user_manager.get_user(user_id):
            print(f"❌ User ID {user_id} already exists!")
            return
        
        name = input("Name: ").strip()
        valid, error = validate_name(name)
        if not valid:
            print(f"❌ {error}")
            return
        
        email = input("Email: ").strip()
        valid, error = validate_email(email)
        if not valid:
            print(f"❌ {error}")
            return
        
        phone = input("Phone (optional): ").strip()
        address = input("Address (optional): ").strip()
        max_loans = input("Max loans (default 5): ").strip() or "5"
        
        try:
            user = User(user_id, name, email, phone, address, max_loans=int(max_loans))
            success, msg = self.user_manager.create_user(user)
            if success:
                print(f"\n✅ {msg}")
                print(user)
            else:
                print(f"\n❌ {msg}")
        except Exception as e:
            print(f"\n❌ Error adding user: {e}")
    
    def _search_user(self):
        """Search for a user"""
        user_id = input("\nEnter User ID: ").strip()
        user = self.user_manager.get_user(user_id)
        
        if user:
            print("\n✅ User found:")
            print(user)
        else:
            print("\n❌ User not found")
    
    def _list_users(self):
        """List all users"""
        users = self.user_manager.list_all_users()
        if not users:
            print("\n👤 No users in system")
            return
        
        print(f"\n👤 USERS ({len(users)} total)")
        print("-"*80)
        for i, user in enumerate(users, 1):
            print(f"\n[{i}]")
            print(user)
    
    def _update_user(self):
        """Update user information"""
        user_id = input("\nEnter User ID to update: ").strip()
        user = self.user_manager.get_user(user_id)
        
        if not user:
            print("❌ User not found")
            return
        
        print(f"\nCurrent information:")
        print(user)
        print("\nEnter new values (press Enter to keep current):")
        
        new_email = input(f"Email ({user.email}): ").strip()
        if new_email:
            valid, error = validate_email(new_email)
            if valid:
                user.email = new_email
        
        print("\n✅ User updated successfully!")
    
    def _delete_user(self):
        """Delete a user"""
        user_id = input("\nEnter User ID to delete: ").strip()
        success, msg = self.user_manager.delete_user(user_id)
        print(f"\n{'✅' if success else '❌'} {msg}")
    
    # ========================================================================
    # LOAN MANAGEMENT
    # ========================================================================
    
    def _loan_management_menu(self):
        """Loan management submenu"""
        while True:
            print("\n" + "-"*80)
            print(" "*30 + "LOAN MANAGEMENT")
            print("-"*80)
            print("1. Loan Book to User")
            print("2. Return Book")
            print("3. View User Loan History")
            print("4. Back to Main Menu")
            
            choice = input("\n👉 Select option: ").strip()
            
            if choice == '1':
                self._loan_book()
            elif choice == '2':
                self._return_book()
            elif choice == '3':
                self._view_loan_history()
            elif choice == '4':
                break
    
    def _loan_book(self):
        """Loan a book to a user"""
        print("\n📖 LOAN BOOK")
        print("-"*80)
        
        user_id = input("User ID: ").strip()
        user = self.user_manager.get_user(user_id)
        if not user:
            print("❌ User not found")
            return
        
        if not user.can_borrow():
            print(f"❌ User has reached maximum loans ({user.max_loans})")
            return
        
        isbn = input("Book ISBN: ").strip()
        success, msg = self.loan_manager.loan_book(user_id, isbn)
        
        if success:
            user.increment_loans()
            print(f"\n✅ {msg}")
        else:
            print(f"\n❌ {msg}")
    
    def _return_book(self):
        """Return a book"""
        print("\n📖 RETURN BOOK")
        print("-"*80)
        
        user_id = input("User ID: ").strip()
        user = self.user_manager.get_user(user_id)
        if not user:
            print("❌ User not found")
            return
        
        isbn = input("Book ISBN: ").strip()
        success, msg = self.loan_manager.return_book(user_id, isbn)
        
        if success:
            user.decrement_loans()
            print(f"\n✅ {msg}")
        else:
            print(f"\n❌ {msg}")
    
    def _view_loan_history(self):
        """View user's loan history"""
        user_id = input("\nEnter User ID: ").strip()
        history = self.loan_manager.get_user_history(user_id)
        
        if history.is_empty():
            print(f"\n📖 No loan history for user {user_id}")
            return
        
        print(f"\n📖 LOAN HISTORY FOR USER {user_id}")
        print("-"*80)
        for i, loan in enumerate(history, 1):
            status = "✅ Returned" if loan.get('returned', False) else "📖 Active"
            print(f"\n[{i}] {status}")
            print(f"    ISBN: {loan['isbn']}")
            print(f"    Title: {loan['title']}")
            print(f"    Loan Date: {loan['loan_date']}")
            if loan.get('returned', False):
                print(f"    Return Date: {loan.get('return_date', 'N/A')}")
    
    # ========================================================================
    # SHELF ANALYSIS (ALGORITHMS)
    # ========================================================================
    
    def _shelf_analysis_menu(self):
        """Shelf analysis submenu"""
        while True:
            print("\n" + "-"*80)
            print(" "*25 + "SHELF ANALYSIS (ALGORITHMS)")
            print("-"*80)
            print("1. Brute Force: Find Risky Combinations (> 8 Kg)")
            print("2. Backtracking: Find Optimal Shelf (Max Value)")
            print("3. Compare Both Approaches")
            print("4. Back to Main Menu")
            
            choice = input("\n👉 Select option: ").strip()
            
            if choice == '1':
                self._run_brute_force()
            elif choice == '2':
                self._run_backtracking()
            elif choice == '3':
                self._compare_algorithms()
            elif choice == '4':
                break
    
    def _run_brute_force(self):
        """Run brute force analysis"""
        books = self.inventory.get_all_books()
        if len(books) < 4:
            print("\n❌ Need at least 4 books for this analysis")
            return
        
        print("\n⏳ Running brute force analysis...")
        results = find_risky_shelf_combinations(books)
        display_risky_combinations(results)
        
        save = input("\n💾 Save report to file? (y/n): ").strip().lower()
        if save == 'y':
            path = generate_risky_combinations_report(results)
            print(f"✅ Report saved to: {path}")
    
    def _run_backtracking(self):
        """Run backtracking optimization"""
        books = self.inventory.get_all_books()
        if not books:
            print("\n❌ No books in inventory")
            return
        
        show_steps = input("\n🔍 Show exploration steps? (y/n): ").strip().lower()
        
        print("\n⏳ Running backtracking optimization...")
        solution = find_optimal_shelf_backtracking(books, show_exploration=(show_steps=='y'))
        display_optimal_solution(solution)
        
        save = input("\n💾 Save report to file? (y/n): ").strip().lower()
        if save == 'y':
            path = generate_optimal_shelf_report(solution)
            print(f"✅ Report saved to: {path}")
    
    def _compare_algorithms(self):
        """Compare brute force vs backtracking"""
        from src.problem_solving.backtracking import compare_backtracking_vs_brute_force
        
        books = self.inventory.get_all_books()
        if not books:
            print("\n❌ No books in inventory")
            return
        
        print("\n⏳ Comparing algorithms...")
        compare_backtracking_vs_brute_force(books[:15])  # Limit to 15 for speed
    
    # ========================================================================
    # RECURSIVE FUNCTIONS
    # ========================================================================
    
    def _recursive_functions_menu(self):
        """Recursive functions demonstration"""
        while True:
            print("\n" + "-"*80)
            print(" "*25 + "RECURSIVE FUNCTIONS DEMO")
            print("-"*80)
            print("1. Stack Recursion: Total Value by Author")
            print("2. Tail Recursion: Average Weight by Author")
            print("3. Back to Main Menu")
            
            choice = input("\n👉 Select option: ").strip()
            
            if choice == '1':
                self._demo_stack_recursion()
            elif choice == '2':
                self._demo_tail_recursion()
            elif choice == '3':
                break
    
    def _demo_stack_recursion(self):
        """Demonstrate stack recursion"""
        author = input("\nEnter author name: ").strip()
        books = self.inventory.get_all_books()
        
        print(f"\n🔄 Calculating total value using STACK RECURSION...")
        total = calculate_total_value_by_author(books, author)
        
        print(f"\n✅ Result:")
        print(f"   Total value of books by '{author}': ${total:,} COP")
    
    def _demo_tail_recursion(self):
        """Demonstrate tail recursion"""
        author = input("\nEnter author name: ").strip()
        books = self.inventory.get_all_books()
        
        print(f"\n🔄 Calculating average weight using TAIL RECURSION...")
        print(f"   (Watch the console output to see tail recursion steps)\n")
        avg = calculate_average_weight_by_author(books, author)
        
        print(f"\n✅ Final Result:")
        print(f"   Average weight of books by '{author}': {avg:.2f} Kg")
    
    # ========================================================================
    # REPORTS
    # ========================================================================
    
    def _generate_reports_menu(self):
        """Generate reports menu"""
        while True:
            print("\n" + "-"*80)
            print(" "*30 + "GENERATE REPORTS")
            print("-"*80)
            print("1. Inventory Report (Sorted by Value)")
            print("2. Back to Main Menu")
            
            choice = input("\n👉 Select option: ").strip()
            
            if choice == '1':
                self._generate_value_report()
            elif choice == '2':
                break
    
    def _generate_value_report(self):
        """Generate inventory report sorted by value"""
        books = self.inventory.generate_value_report()
        
        print(f"\n📊 INVENTORY REPORT (Sorted by Value - Descending)")
        print("="*80)
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Books: {len(books)}")
        print("="*80)
        
        total_value = sum(book.value for book in books)
        total_weight = sum(book.weight for book in books)
        
        for i, book in enumerate(books, 1):
            print(f"\n[{i}] ${book.value:,} COP - {book.title}")
            print(f"    Author: {book.author}")
            print(f"    ISBN: {book.isbn}")
            print(f"    Weight: {book.weight} Kg, Stock: {book.stock}")
        
        print("\n" + "="*80)
        print(f"TOTALS:")
        print(f"  Total Value: ${total_value:,} COP")
        print(f"  Total Weight: {total_weight:.2f} Kg")
        print(f"  Average Value: ${total_value // len(books):,} COP")
        print("="*80)
        
        save = input("\n💾 Save report to file? (y/n): ").strip().lower()
        if save == 'y':
            filename = 'reports/inventory_value_report.txt'
            os.makedirs('reports', exist_ok=True)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("INVENTORY REPORT (Sorted by Value)\n")
                f.write("="*80 + "\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Books: {len(books)}\n\n")
                
                for i, book in enumerate(books, 1):
                    f.write(f"[{i}] ${book.value:,} COP - {book.title}\n")
                    f.write(f"    Author: {book.author}\n")
                    f.write(f"    ISBN: {book.isbn}\n")
                    f.write(f"    Weight: {book.weight} Kg, Stock: {book.stock}\n\n")
                
                f.write("="*80 + "\n")
                f.write(f"Total Value: ${total_value:,} COP\n")
                f.write(f"Total Weight: {total_weight:.2f} Kg\n")
            
            print(f"✅ Report saved to: {filename}")


def main():
    """Main entry point"""
    try:
        lms = LibraryManagementSystem()
        lms.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
