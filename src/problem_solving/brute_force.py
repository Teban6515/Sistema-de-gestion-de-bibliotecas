"""
Brute Force Algorithm - Deficient Shelf

This module implements a brute force algorithm to find all combinations
of 4 books that exceed the maximum weight capacity of 8 Kg.

Author: Miguel Bravo
Date: December 2025
Course: Programming Techniques
"""

from itertools import combinations


def find_risky_shelf_combinations(books_list, max_weight=8.0, combination_size=4):
    """
    Find all combinations of 4 books that exceed the weight threshold using BRUTE FORCE.
    
    This algorithm exhaustively explores ALL possible combinations of 4 books
    to identify those that would overload a shelf (exceed 8 Kg).
    
    Args:
        books_list (list): List of Book objects
        max_weight (float): Maximum safe weight capacity in Kg (default: 8.0)
        combination_size (int): Number of books per combination (default: 4)
    
    Returns:
        list: List of dictionaries containing risky combinations with:
            - 'books': tuple of Book objects
            - 'total_weight': total weight in Kg
            - 'excess_weight': how much it exceeds the limit
            - 'total_value': total value in COP
            - 'isbns': list of ISBNs for reference
    
    Time Complexity: O(C(n,4)) = O(n^4 / 24) ≈ O(n^4)
        - For n=25 books: C(25,4) = 12,650 combinations
        - For n=50 books: C(50,4) = 230,300 combinations
    
    Space Complexity: O(k) where k is number of risky combinations found
    
    Algorithm (Brute Force):
        1. Generate ALL combinations of 4 books
        2. For EACH combination:
           a. Calculate total weight
           b. Check if exceeds threshold
           c. Store if risky
        3. Return all risky combinations
    
    Example:
        If we have books with weights [2.0, 2.5, 3.0, 3.5, 1.5]:
        - Combination (2.0, 2.5, 3.0, 3.5) = 11.0 Kg → RISKY (exceeds 8 Kg)
        - Combination (2.0, 2.5, 3.0, 1.5) = 9.0 Kg → RISKY (exceeds 8 Kg)
        - Combination (2.0, 2.5, 1.5, 3.0) = 9.0 Kg → RISKY (exceeds 8 Kg)
    """
    risky_combinations = []
    total_combinations_checked = 0
    
    # Generate ALL combinations of the specified size
    for combo in combinations(books_list, combination_size):
        total_combinations_checked += 1
        
        # Calculate total weight and value
        total_weight = sum(book.weight for book in combo)
        total_value = sum(book.value for book in combo)
        
        # Check if this combination exceeds the weight limit
        if total_weight > max_weight:
            risky_combinations.append({
                'books': combo,
                'total_weight': round(total_weight, 2),
                'excess_weight': round(total_weight - max_weight, 2),
                'total_value': total_value,
                'isbns': [book.isbn for book in combo],
                'titles': [book.title for book in combo]
            })
    
    # Sort by excess weight (most dangerous first)
    risky_combinations.sort(key=lambda x: x['excess_weight'], reverse=True)
    
    return {
        'risky_combinations': risky_combinations,
        'total_checked': total_combinations_checked,
        'risky_count': len(risky_combinations),
        'risk_percentage': (len(risky_combinations) / total_combinations_checked * 100) 
                          if total_combinations_checked > 0 else 0
    }


def find_all_overweight_combinations(books_list, max_weight=8.0):
    """
    Find ALL overweight combinations of ANY size (not just 4 books).
    
    WARNING: This is VERY expensive computationally!
    For n books, this checks 2^n - 1 combinations.
    
    Args:
        books_list (list): List of Book objects
        max_weight (float): Maximum weight capacity
    
    Returns:
        dict: Categorized results by combination size
    
    Time Complexity: O(2^n) - exponential!
        - For n=10: 1,024 combinations
        - For n=20: 1,048,576 combinations
        - For n=25: 33,554,432 combinations (VERY SLOW!)
    """
    results_by_size = {}
    total_checked = 0
    
    # Check combinations of each size from 1 to n
    for size in range(1, len(books_list) + 1):
        risky = []
        
        for combo in combinations(books_list, size):
            total_checked += 1
            total_weight = sum(book.weight for book in combo)
            
            if total_weight > max_weight:
                risky.append({
                    'books': combo,
                    'total_weight': round(total_weight, 2),
                    'excess_weight': round(total_weight - max_weight, 2)
                })
        
        if risky:
            results_by_size[size] = risky
    
    return {
        'results_by_size': results_by_size,
        'total_checked': total_checked
    }


def display_risky_combinations(results, max_display=10):
    """
    Display risky combinations in a formatted way.
    
    Args:
        results (dict): Results from find_risky_shelf_combinations
        max_display (int): Maximum number of combinations to display
    """
    print("\n" + "="*80)
    print("BRUTE FORCE ANALYSIS: RISKY SHELF COMBINATIONS")
    print("="*80)
    
    risky = results['risky_combinations']
    
    print(f"\n📊 STATISTICS:")
    print(f"   Total combinations checked: {results['total_checked']:,}")
    print(f"   Risky combinations found: {results['risky_count']:,}")
    print(f"   Risk percentage: {results['risk_percentage']:.2f}%")
    
    if not risky:
        print("\n✅ No risky combinations found! All combinations are safe.")
        return
    
    print(f"\n⚠️  TOP {min(max_display, len(risky))} MOST DANGEROUS COMBINATIONS:")
    print("-"*80)
    
    for i, combo in enumerate(risky[:max_display], 1):
        print(f"\n[{i}] EXCESS WEIGHT: {combo['excess_weight']:.2f} Kg over limit")
        print(f"    Total Weight: {combo['total_weight']:.2f} Kg")
        print(f"    Total Value: ${combo['total_value']:,} COP")
        print(f"    Books:")
        for book in combo['books']:
            print(f"      • {book.title[:50]}")
            print(f"        ISBN: {book.isbn}, Weight: {book.weight} Kg, Value: ${book.value:,}")
    
    if len(risky) > max_display:
        print(f"\n... and {len(risky) - max_display} more risky combinations.")


def generate_risky_combinations_report(results, filename='reports/risky_combinations.txt'):
    """
    Generate a text report of risky combinations.
    
    Args:
        results (dict): Results from find_risky_shelf_combinations
        filename (str): Output file path
    
    Returns:
        str: Path to generated report
    """
    import os
    from datetime import datetime
    
    # Ensure reports directory exists
    os.makedirs('reports', exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("BRUTE FORCE ANALYSIS: RISKY SHELF COMBINATIONS REPORT\n")
        f.write("="*80 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Maximum Safe Weight: 8.0 Kg\n")
        f.write(f"Combination Size: 4 books\n\n")
        
        f.write("STATISTICS\n")
        f.write("-"*80 + "\n")
        f.write(f"Total combinations checked: {results['total_checked']:,}\n")
        f.write(f"Risky combinations found: {results['risky_count']:,}\n")
        f.write(f"Risk percentage: {results['risk_percentage']:.2f}%\n\n")
        
        if results['risky_combinations']:
            f.write("RISKY COMBINATIONS (sorted by excess weight)\n")
            f.write("-"*80 + "\n\n")
            
            for i, combo in enumerate(results['risky_combinations'], 1):
                f.write(f"[{i}] Excess Weight: {combo['excess_weight']:.2f} Kg\n")
                f.write(f"    Total Weight: {combo['total_weight']:.2f} Kg\n")
                f.write(f"    Total Value: ${combo['total_value']:,} COP\n")
                f.write(f"    Books:\n")
                for book in combo['books']:
                    f.write(f"      • {book.title}\n")
                    f.write(f"        ISBN: {book.isbn}\n")
                    f.write(f"        Weight: {book.weight} Kg, Value: ${book.value:,} COP\n")
                f.write("\n")
        else:
            f.write("✅ No risky combinations found! All combinations are safe.\n")
    
    return filename


# Testing module
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    
    from src.models.book import Book
    
    # Create test books with various weights
    test_books = [
        Book("978-1", "Heavy Book A", "Author 1", 2.8, 100000, 1),
        Book("978-2", "Heavy Book B", "Author 2", 2.5, 120000, 1),
        Book("978-3", "Heavy Book C", "Author 3", 2.2, 90000, 1),
        Book("978-4", "Heavy Book D", "Author 4", 2.0, 80000, 1),
        Book("978-5", "Light Book E", "Author 5", 1.0, 60000, 1),
        Book("978-6", "Light Book F", "Author 6", 0.8, 50000, 1),
    ]
    
    print("=== Testing Brute Force Algorithm ===\n")
    print("Test Books:")
    for book in test_books:
        print(f"  {book.title}: {book.weight} Kg")
    
    print(f"\nTotal combinations of 4 books from {len(test_books)} books:")
    from math import comb
    print(f"  C({len(test_books)}, 4) = {comb(len(test_books), 4)} combinations")
    
    # Run brute force analysis
    results = find_risky_shelf_combinations(test_books)
    
    # Display results
    display_risky_combinations(results)
    
    # Generate report
    report_path = generate_risky_combinations_report(results)
    print(f"\n📄 Report generated: {report_path}")
