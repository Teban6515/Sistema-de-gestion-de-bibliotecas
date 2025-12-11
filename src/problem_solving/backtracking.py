"""
Backtracking Algorithm - Optimal Shelf

This module implements a backtracking algorithm to find the combination
of books that maximizes total value without exceeding 8 Kg weight capacity.

Author: Miguel Bravo
Date: December 2025
Course: Programming Techniques
"""

### Encuentra la combinación óptima con PODA eficiente
def find_optimal_shelf_backtracking(books_list, max_weight=8.0, show_exploration=False):
    """
    Find the optimal combination of books that maximizes value using BACKTRACKING.
    
    This algorithm uses backtracking with pruning to efficiently explore
    the solution space and find the best combination without exceeding weight limit.
    
    Args:
        books_list (list): List of Book objects
        max_weight (float): Maximum weight capacity in Kg (default: 8.0)
        show_exploration (bool): Print exploration steps for demonstration
    
    Returns:
        dict: Optimal solution containing:
            - 'books': list of Book objects in optimal combination
            - 'total_value': total value in COP
            - 'total_weight': total weight in Kg
            - 'book_count': number of books
            - 'isbns': list of ISBNs
            - 'exploration_count': number of nodes explored
            - 'pruning_count': number of branches pruned
    
    Time Complexity: O(2^n) worst case, but typically much better with pruning
    Space Complexity: O(n) for recursion call stack
    
    Algorithm (Backtracking with Pruning):
        1. For each book, try two choices:
           a. Include it (if weight allows)
           b. Exclude it
        2. Track best solution found so far
        3. Prune branches that:
           - Would exceed weight limit
           - Cannot possibly beat best solution
        4. Return optimal solution
    
    Backtracking Demonstration:
        The algorithm explores a decision tree where each level represents
        a book and each branch represents include/exclude decisions.
        
        Example tree (simplified):
                      Root
                    /      \\
              Include B1   Exclude B1
               /    \\        /    \\
          +B2    -B2      +B2    -B2
           ...    ...      ...    ...
    """
    # Sort books by value/weight ratio (greedy heuristic for better pruning)
    # Ordenar libros por la relación valor/peso (heurística codiciosa para una mejor poda)
    sorted_books = sorted(books_list, key=lambda b: b.value / b.weight, reverse=True)
    
    best_solution = {
        'books': [],
        'total_value': 0,
        'total_weight': 0,
        'book_count': 0,
        'isbns': []
    }
    # Usar lista para mantener referencia en función anidada
    exploration_count = [0]  # Use list to maintain reference in nested function
    pruning_count = [0]
    
    def backtrack(index, current_books, current_weight, current_value, depth=0):
        """
        Recursive backtracking function.
        
        Args:
            index: Current book index being considered
            current_books: Books in current partial solution
            current_weight: Current total weight
            current_value: Current total value
            depth: Recursion depth (for visualization)
        """
        nonlocal best_solution
        exploration_count[0] += 1
        
        # Display exploration step if requested
        if show_exploration:
            indent = "  " * depth
            print(f"{indent}[Node {exploration_count[0]}] Exploring index {index}, "
                  f"Weight: {current_weight:.2f}/{max_weight} Kg, "
                  f"Value: ${current_value:,}")
        
        # Comprobar si la solución actual es mejor que la mejor encontrada hasta el momento
        # Check if current solution is better than best found so far
        if current_value > best_solution['total_value']:
            best_solution = {
                'books': current_books.copy(),
                'total_value': current_value,
                'total_weight': current_weight,
                'book_count': len(current_books),
                'isbns': [book.isbn for book in current_books]
            }
            if show_exploration:
                print(f"{indent}✨ NEW BEST: ${current_value:,} COP")

        # Caso base: se han considerado todos los libros
        # Base case: all books have been considered
        if index >= len(sorted_books):
            return
        
        current_book = sorted_books[index]
        # PODA 1: Comprobar si añadir este libro excedería el peso
        # PRUNING 1: Check if adding this book would exceed weight
        if current_weight + current_book.weight <= max_weight:
            # OPCIÓN 1: INCLUIR el libro actual
            # CHOICE 1: INCLUDE current book
            if show_exploration:
                print(f"{indent}↓ Including: {current_book.title[:30]}")
            
            current_books.append(current_book)
            backtrack(index + 1, current_books, 
                     current_weight + current_book.weight,
                     current_value + current_book.value,
                     depth + 1)
            current_books.pop()  # BACKTRACK

            if show_exploration:
                print(f"{indent}↑ Backtracking from include")
        else:
            # Prune this branch
            pruning_count[0] += 1
            if show_exploration:
                print(f"{indent}✂️ PRUNED: Would exceed weight limit")
                
        # PODA 2: Comprobación del límite optimista
        # Calcular el límite superior: valor actual + valores de todos los libros restantes
        # PRUNING 2: Optimistic bound check
        # Calculate upper bound: current value + all remaining books' values
        remaining_value = sum(book.value for book in sorted_books[index + 1:])
        if current_value + remaining_value <= best_solution['total_value']:
            pruning_count[0] += 1
            if show_exploration:
                print(f"{indent}✂️ PRUNED: Cannot beat current best")
            return
        
        # CHOICE 2: EXCLUDE current book
        if show_exploration:
            print(f"{indent}→ Excluding: {current_book.title[:30]}")
        
        backtrack(index + 1, current_books, current_weight, current_value, depth + 1)
    
    # Start backtracking from index 0
    if show_exploration:
        print("\n" + "="*80)
        print("BACKTRACKING EXPLORATION")
        print("="*80)
    
    backtrack(0, [], 0, 0)
    
    # Add exploration statistics
    best_solution['exploration_count'] = exploration_count[0]
    best_solution['pruning_count'] = pruning_count[0]
    best_solution['efficiency'] = (1 - exploration_count[0] / (2 ** len(books_list))) * 100
    
    return best_solution


def find_optimal_shelf_dynamic(books_list, max_weight=8.0):
    """
    Alternative implementation using dynamic programming (0/1 Knapsack).
    
    This is more efficient than pure backtracking for this specific problem.
    
    Args:
        books_list (list): List of Book objects
        max_weight (float): Maximum weight capacity
    
    Returns:
        dict: Optimal solution
    
    Time Complexity: O(n * W) where W is max_weight * 10 (for precision)
    Space Complexity: O(n * W)
    
    Note: This demonstrates an alternative approach that's often better
    than backtracking for knapsack-type problems.
    """
    n = len(books_list)
    # Convert weight to integer (multiply by 10 for 1 decimal precision)
    W = int(max_weight * 10)
    
    # Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        book = books_list[i - 1]
        book_weight = int(book.weight * 10)
        
        for w in range(W + 1):
            # Don't include current book
            dp[i][w] = dp[i - 1][w]
            
            # Include current book if it fits
            if book_weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - book_weight] + book.value)
    
    # Backtrack to find which books were selected
    selected_books = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_books.append(books_list[i - 1])
            w -= int(books_list[i - 1].weight * 10)
    
    selected_books.reverse()
    
    return {
        'books': selected_books,
        'total_value': dp[n][W],
        'total_weight': sum(book.weight for book in selected_books),
        'book_count': len(selected_books),
        'isbns': [book.isbn for book in selected_books],
        'method': 'Dynamic Programming'
    }


def compare_backtracking_vs_brute_force(books_list, max_weight=8.0):
    """
    Compare backtracking efficiency vs brute force.
    
    Args:
        books_list (list): List of Book objects
        max_weight (float): Maximum weight capacity
    
    Returns:
        dict: Comparison results
    """
    from itertools import combinations
    import time
    
    n = len(books_list)
    total_combinations = 2 ** n - 1
    
    print("\n" + "="*80)
    print("BACKTRACKING vs BRUTE FORCE COMPARISON")
    print("="*80)
    print(f"Number of books: {n}")
    print(f"Total possible combinations: {total_combinations:,}\n")
    
    # Time backtracking
    start = time.time()
    bt_result = find_optimal_shelf_backtracking(books_list, max_weight, show_exploration=False)
    bt_time = time.time() - start
    
    print(f"Backtracking:")
    print(f"  Nodes explored: {bt_result['exploration_count']:,}")
    print(f"  Branches pruned: {bt_result['pruning_count']:,}")
    print(f"  Efficiency: {bt_result['efficiency']:.2f}% less exploration than brute force")
    print(f"  Time: {bt_time:.6f} seconds")
    print(f"  Best value: ${bt_result['total_value']:,} COP")
    print(f"  Best weight: {bt_result['total_weight']:.2f} Kg")
    
    # Time brute force (only for small n)
    if n <= 20:
        start = time.time()
        best_value = 0
        best_combo = []
        checked = 0
        
        for r in range(1, n + 1):
            for combo in combinations(books_list, r):
                checked += 1
                weight = sum(book.weight for book in combo)
                if weight <= max_weight:
                    value = sum(book.value for book in combo)
                    if value > best_value:
                        best_value = value
                        best_combo = combo
        
        bf_time = time.time() - start
        
        print(f"\nBrute Force:")
        print(f"  Combinations checked: {checked:,}")
        print(f"  Time: {bf_time:.6f} seconds")
        print(f"  Best value: ${best_value:,} COP")
        
        print(f"\nSpeedup: {bf_time / bt_time:.2f}x faster with backtracking")
    else:
        print(f"\nBrute force skipped (too many books: {n})")
    
    return bt_result


def display_optimal_solution(solution):
    """
    Display the optimal solution in a formatted way.
    
    Args:
        solution (dict): Solution from find_optimal_shelf_backtracking
    """
    print("\n" + "="*80)
    print("OPTIMAL SHELF CONFIGURATION (BACKTRACKING)")
    print("="*80)
    
    print(f"\n📊 OPTIMIZATION STATISTICS:")
    print(f"   Nodes explored: {solution.get('exploration_count', 'N/A'):,}")
    print(f"   Branches pruned: {solution.get('pruning_count', 'N/A'):,}")
    if 'efficiency' in solution:
        print(f"   Efficiency gain: {solution['efficiency']:.2f}%")
    
    print(f"\n✨ OPTIMAL SOLUTION:")
    print(f"   Total Value: ${solution['total_value']:,} COP")
    print(f"   Total Weight: {solution['total_weight']:.2f} Kg / 8.0 Kg")
    print(f"   Remaining Capacity: {8.0 - solution['total_weight']:.2f} Kg")
    print(f"   Number of Books: {solution['book_count']}")
    
    print(f"\n📚 BOOKS IN OPTIMAL COMBINATION:")
    print("-"*80)
    
    for i, book in enumerate(solution['books'], 1):
        print(f"\n[{i}] {book.title}")
        print(f"    Author: {book.author}")
        print(f"    ISBN: {book.isbn}")
        print(f"    Weight: {book.weight} Kg")
        print(f"    Value: ${book.value:,} COP")
        print(f"    Value/Weight Ratio: ${book.value / book.weight:,.2f} per Kg")


def generate_optimal_shelf_report(solution, filename='reports/optimal_shelf.txt'):
    """
    Generate a text report of the optimal shelf configuration.
    
    Args:
        solution (dict): Solution from find_optimal_shelf_backtracking
        filename (str): Output file path
    
    Returns:
        str: Path to generated report
    """
    import os
    from datetime import datetime
    
    os.makedirs('reports', exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("BACKTRACKING OPTIMIZATION: OPTIMAL SHELF CONFIGURATION\n")
        f.write("="*80 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Maximum Weight Capacity: 8.0 Kg\n\n")
        
        f.write("OPTIMIZATION STATISTICS\n")
        f.write("-"*80 + "\n")
        f.write(f"Nodes explored: {solution.get('exploration_count', 'N/A'):,}\n")
        f.write(f"Branches pruned: {solution.get('pruning_count', 'N/A'):,}\n")
        if 'efficiency' in solution:
            f.write(f"Efficiency gain: {solution['efficiency']:.2f}%\n")
        f.write("\n")
        
        f.write("OPTIMAL SOLUTION\n")
        f.write("-"*80 + "\n")
        f.write(f"Total Value: ${solution['total_value']:,} COP\n")
        f.write(f"Total Weight: {solution['total_weight']:.2f} Kg\n")
        f.write(f"Remaining Capacity: {8.0 - solution['total_weight']:.2f} Kg\n")
        f.write(f"Number of Books: {solution['book_count']}\n\n")
        
        f.write("BOOKS IN OPTIMAL COMBINATION\n")
        f.write("-"*80 + "\n\n")
        
        for i, book in enumerate(solution['books'], 1):
            f.write(f"[{i}] {book.title}\n")
            f.write(f"    Author: {book.author}\n")
            f.write(f"    ISBN: {book.isbn}\n")
            f.write(f"    Weight: {book.weight} Kg\n")
            f.write(f"    Value: ${book.value:,} COP\n")
            f.write(f"    Value/Weight Ratio: ${book.value / book.weight:,.2f} per Kg\n\n")
    
    return filename


# Testing module
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    
    from src.models.book import Book
    
    # Create test books
    test_books = [
        Book("978-1", "Expensive Light Book", "Author 1", 1.0, 200000, 1),
        Book("978-2", "Cheap Heavy Book", "Author 2", 3.0, 50000, 1),
        Book("978-3", "Medium Book A", "Author 3", 2.0, 150000, 1),
        Book("978-4", "Medium Book B", "Author 4", 2.5, 180000, 1),
        Book("978-5", "Light Valuable", "Author 5", 0.8, 120000, 1),
        Book("978-6", "Heavy Valuable", "Author 6", 3.5, 250000, 1),
    ]
    
    print("=== Testing Backtracking Algorithm ===\n")
    print("Test Books:")
    for book in test_books:
        print(f"  {book.title}: {book.weight} Kg, ${book.value:,} COP, "
              f"Ratio: ${book.value/book.weight:,.0f}/Kg")
    
    # Run backtracking with exploration display
    print("\n" + "="*80)
    print("Running backtracking WITH exploration display (first 3 levels)...")
    print("="*80)
    solution = find_optimal_shelf_backtracking(test_books[:4], show_exploration=True)
    
    # Display solution
    display_optimal_solution(solution)
    
    # Generate report
    report_path = generate_optimal_shelf_report(solution)
    print(f"\n📄 Report generated: {report_path}")
    
    # Compare with full dataset
    print("\n" + "="*80)
    print("Running full optimization...")
    print("="*80)
    full_solution = find_optimal_shelf_backtracking(test_books, show_exploration=False)
    display_optimal_solution(full_solution)
