

def find_optimal_shelf_with_weight_constraint(books_list, max_weight=8.0, 
                                               min_book_weight=0.5,
                                               show_exploration=False):
    
    # Sort books by value/weight ratio for better performance
    sorted_books = sorted(books_list, key=lambda b: b.value / b.weight, reverse=True)
    
    best_solution = {
        'books': [],
        'total_value': 0,
        'total_weight': 0,
        'book_count': 0,
        'isbns': []
    }
    
    exploration_count = [0]
    pruning_count = [0]
    weight_constraint_pruned = [0]  # NEW: Track how many pruned by weight rule
    
    def backtrack(index, current_books, current_weight, current_value, depth=0):
        """Recursive backtracking with weight constraint pruning."""
        nonlocal best_solution
        exploration_count[0] += 1
        
        if show_exploration:
            indent = "  " * depth
            print(f"{indent}[Node {exploration_count[0]}] Index {index}, "
                  f"Weight: {current_weight:.2f}/{max_weight}, "
                  f"Value: ${current_value:,}")
        
        # Update best solution if current is better
        if current_value > best_solution['total_value']:
            best_solution = {
                'books': current_books.copy(),
                'total_value': current_value,
                'total_weight': current_weight,
                'book_count': len(current_books),
                'isbns': [book.isbn for book in current_books]
            }
            if show_exploration:
                print(f"{indent}✨ NEW BEST: ${current_value:,}")
        
        # BASE CASE: All books considered
        if index >= len(sorted_books):
            return
        
        current_book = sorted_books[index]
        
        # =====================================================================
        # PODA 1: WEIGHT CONSTRAINT (NEW!)
        # Books with weight < min_book_weight are IGNORED
        # This happens FIRST, before any other checks
        # =====================================================================
        if current_book.weight < min_book_weight:
            weight_constraint_pruned[0] += 1
            pruning_count[0] += 1
            
            if show_exploration:
                print(f"{indent}✂️ WEIGHT CONSTRAINT PRUNED: {current_book.title[:30]}")
                print(f"{indent}   Weight {current_book.weight} < {min_book_weight} Kg")
            
            # Skip this book entirely - move to next
            backtrack(index + 1, current_books, current_weight, current_value, depth)
            return  # Don't consider including this book at all
        
        # =====================================================================
        # PODA 2: CAPACITY CHECK
        # Can this book fit in remaining capacity?
        # =====================================================================
        if current_weight + current_book.weight <= max_weight:
            # CHOICE 1: INCLUDE current book
            if show_exploration:
                print(f"{indent}↓ Including: {current_book.title[:30]} "
                      f"({current_book.weight} Kg, ${current_book.value:,})")
            
            current_books.append(current_book)
            backtrack(index + 1, current_books, 
                     current_weight + current_book.weight,
                     current_value + current_book.value,
                     depth + 1)
            current_books.pop()  # BACKTRACK
            
            if show_exploration:
                print(f"{indent}↑ Backtracked from include")
        else:
            # Book doesn't fit - prune this branch
            pruning_count[0] += 1
            if show_exploration:
                print(f"{indent}✂️ CAPACITY PRUNED: Would exceed {max_weight} Kg")
        
        # =====================================================================
        # PODA 3: OPTIMISTIC BOUND
        # Can remaining books improve solution?
        # =====================================================================
        remaining_value = sum(b.value for b in sorted_books[index + 1:] 
                             if b.weight >= min_book_weight)  # Only count valid books
        
        if current_value + remaining_value <= best_solution['total_value']:
            pruning_count[0] += 1
            if show_exploration:
                print(f"{indent}✂️ BOUND PRUNED: Cannot beat current best")
            return
        
        # CHOICE 2: EXCLUDE current book
        if show_exploration:
            print(f"{indent}→ Excluding: {current_book.title[:30]}")
        
        backtrack(index + 1, current_books, current_weight, current_value, depth + 1)
    
    # Start backtracking
    if show_exploration:
        print("\n" + "="*80)
        print("BACKTRACKING WITH WEIGHT CONSTRAINT PRUNING")
        print("="*80)
        print(f"Minimum book weight: {min_book_weight} Kg")
        print(f"Books below this weight will be IGNORED")
        print("="*80 + "\n")
    
    backtrack(0, [], 0, 0)
    
    # Add statistics
    best_solution['exploration_count'] = exploration_count[0]
    best_solution['pruning_count'] = pruning_count[0]
    best_solution['weight_constraint_pruned'] = weight_constraint_pruned[0]
    best_solution['efficiency'] = (1 - exploration_count[0] / (2 ** len(books_list))) * 100
    best_solution['min_book_weight'] = min_book_weight
    
    return best_solution

