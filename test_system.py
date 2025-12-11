"""Quick test script to verify the system works"""
import sys
import os

def test_system():
    print("="*80)
    print(" "*25 + "SYSTEM VERIFICATION TEST")
    print("="*80)
    
    errors = []
    
    # Test 1: Check Python version
    print("\n[1] Checking Python version...")
    if sys.version_info >= (3, 8):
        print(f"    ✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    else:
        print(f"    ❌ Python version too old: {sys.version}")
        errors.append("Python version < 3.8")
    
    # Test 2: Check required files
    print("\n[2] Checking required files...")
    required_files = [
        'main.py',
        'data/books.json',
        'data/users.json',
        'src/models/book.py',
        'src/algorithms/sorting.py'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"    ✅ {file}")
        else:
            print(f"    ❌ {file} NOT FOUND")
            errors.append(f"Missing file: {file}")
    
    # Test 3: Try importing modules
    print("\n[3] Testing module imports...")
    try:
        sys.path.insert(0, 'src')
        from models.book import Book
        print("    ✅ Book model")
        
        from data_structures.stack import Stack
        print("    ✅ Stack structure")
        
        from algorithms.sorting import insertion_sort_by_isbn
        print("    ✅ Sorting algorithms")
        
        from problem_solving.brute_force import find_risky_shelf_combinations
        print("    ✅ Brute force")
        
        from problem_solving.backtracking import find_optimal_shelf_backtracking
        print("    ✅ Backtracking")
        
    except Exception as e:
        print(f"    ❌ Import error: {e}")
        errors.append(f"Import error: {e}")
    
    # Test 4: Create test objects
    print("\n[4] Testing object creation...")
    try:
        book = Book("978-TEST", "Test Book", "Test Author", 1.0, 10000, 1)
        print(f"    ✅ Created test book: {book.title}")
        
        stack = Stack()
        stack.push("test")
        print(f"    ✅ Stack operations work")
        
    except Exception as e:
        print(f"    ❌ Object creation error: {e}")
        errors.append(f"Object error: {e}")
    
    # Summary
    print("\n" + "="*80)
    if not errors:
        print("✅ ALL TESTS PASSED! System is ready to run.")
        print("\nTo start the system, run:")
        print("    python main.py")
    else:
        print(f"❌ {len(errors)} ERROR(S) FOUND:")
        for error in errors:
            print(f"   • {error}")
    print("="*80)

if __name__ == "__main__":
    test_system()
