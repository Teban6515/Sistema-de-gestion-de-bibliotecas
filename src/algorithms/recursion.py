"""
Recursive Functions

This module implements recursive functions for the Library Management System:
- Stack Recursion: Calculate total value of books by author
- Tail Recursion: Calculate average weight of books by author

Author: [Your Name]
Date: December 2025
Course: Programming Techniques
"""
###recurcion de pila ...y de cola vs
##Pila: return valor + recursion() - opera después

##Cola: return recursion(nuevo_estado) - opera antes

###Calcular el valor total de los libros de un autor específico usando recursión de pila.
def calculate_total_value_by_author(books_list, author, index=0):
  
    # Base case: reached end of list
    if index >= len(books_list):
        return 0
    
    # Get current book
    current_book = books_list[index]
    
    # Recursive case: check if book matches author
    if current_book.author.lower() == author.lower():
        # Add current book's value to sum of remaining books
        # NOTE: Addition happens AFTER recursive call returns (stack recursion)
        return current_book.value + calculate_total_value_by_author(books_list, author, index + 1)
    else:
        # Skip this book, continue with next
        return calculate_total_value_by_author(books_list, author, index + 1)

###Calcular el peso promedio de los libros de un autor específico usando recursión de cola.
def calculate_average_weight_by_author(books_list, author, index=0, total_weight=0, count=0):

    # Base case: reached end of list
    if index >= len(books_list):
        # Calculate and return average
        if count == 0:
            print(f"[Base case] No books found by author '{author}'")
            return 0.0
        
        average = total_weight / count
        print(f"[Base case] Total weight: {total_weight:.2f} Kg, "
              f"Count: {count} books, Average: {average:.2f} Kg")
        return average
    
    # Get current book
    current_book = books_list[index]
    
    # Check if book matches author
    if current_book.author.lower() == author.lower():
        # Print step for demonstration
        new_total = total_weight + current_book.weight
        new_count = count + 1
        print(f"[Step {index}] Processing: '{current_book.title}', "
              f"Weight: {current_book.weight} Kg, "
              f"Running total: {new_total:.2f} Kg, Count: {new_count}")
        
        # TAIL RECURSION: recursive call is the LAST operation
        # All calculations done BEFORE the call
        return calculate_average_weight_by_author(books_list, author, index + 1, new_total, new_count)
    else:
        # Skip this book (different author)
        print(f"[Step {index}] Skipping: '{current_book.title}' (author: {current_book.author})")
        
        # TAIL RECURSION: recursive call is the LAST operation
        return calculate_average_weight_by_author(books_list, author, index + 1, total_weight, count)


def demonstrate_tail_recursion_conversion(books_list, author):
    """
    Demonstrate how tail recursion can be easily converted to iteration.
    
    This function shows the iterative equivalent of calculate_average_weight_by_author,
    proving that tail recursion is mechanically translatable to loops.
    
    Args:
        books_list (list): List of Book objects
        author (str): Author name to filter by
    
    Returns:
        float: Average weight of books by the author
    """
    print("\n=== Iterative version (equivalent to tail recursion) ===")
    
    total_weight = 0
    count = 0
    
    for index, book in enumerate(books_list):
        if book.author.lower() == author.lower():
            total_weight += book.weight
            count += 1
            print(f"[Step {index}] Processing: '{book.title}', "
                  f"Weight: {book.weight} Kg, "
                  f"Running total: {total_weight:.2f} Kg, Count: {count}")
        else:
            print(f"[Step {index}] Skipping: '{book.title}' (author: {book.author})")
    
    if count == 0:
        print(f"[Result] No books found by author '{author}'")
        return 0.0
    
    average = total_weight / count
    print(f"[Result] Total weight: {total_weight:.2f} Kg, "
          f"Count: {count} books, Average: {average:.2f} Kg")
    return average


def count_books_by_author_stack(books_list, author, index=0):
    """
    Count books by author using stack recursion (for comparison).
    
    Args:
        books_list (list): List of Book objects
        author (str): Author name
        index (int): Current index
    
    Returns:
        int: Number of books by the author
    """
    if index >= len(books_list):
        return 0
    
    if books_list[index].author.lower() == author.lower():
        return 1 + count_books_by_author_stack(books_list, author, index + 1)
    else:
        return count_books_by_author_stack(books_list, author, index + 1)


def count_books_by_author_tail(books_list, author, index=0, count=0):
    """
    Count books by author using tail recursion (for comparison).
    
    Args:
        books_list (list): List of Book objects
        author (str): Author name
        index (int): Current index
        count (int): Accumulator for count
    
    Returns:
        int: Number of books by the author
    """
    if index >= len(books_list):
        return count
    
    if books_list[index].author.lower() == author.lower():
        return count_books_by_author_tail(books_list, author, index + 1, count + 1)
    else:
        return count_books_by_author_tail(books_list, author, index + 1, count)


# Testing module
if __name__ == "__main__":
    import sys
    sys.path.append('../..')
    from src.models.book import Book
    
    # Create test books
    books = [
        Book("978-1", "Clean Code", "Robert C. Martin", 0.8, 125000, 3),
        Book("978-2", "The Pragmatic Programmer", "Andrew Hunt", 0.65, 110000, 2),
        Book("978-3", "Clean Architecture", "Robert C. Martin", 0.75, 135000, 2),
        Book("978-4", "Refactoring", "Martin Fowler", 0.9, 145000, 1),
        Book("978-5", "Code Complete", "Steve McConnell", 1.1, 160000, 2),
    ]
    
    print("=== Testing Recursive Functions ===\n")
    print("Books in inventory:")
    for book in books:
        print(f"  {book.title} by {book.author} - Weight: {book.weight} Kg, Value: ${book.value}")
    
    # Test Stack Recursion
    print("\n" + "="*60)
    print("STACK RECURSION: Total value of books by 'Robert C. Martin'")
    print("="*60)
    total_value = calculate_total_value_by_author(books, "Robert C. Martin")
    print(f"\nResult: ${total_value:,} COP")
    
    # Test Tail Recursion
    print("\n" + "="*60)
    print("TAIL RECURSION: Average weight of books by 'Robert C. Martin'")
    print("="*60)
    average_weight = calculate_average_weight_by_author(books, "Robert C. Martin")
    print(f"\nResult: {average_weight:.2f} Kg")
    
    # Demonstrate conversion to iteration
    print("\n" + "="*60)
    print("DEMONSTRATION: Tail recursion → Iteration conversion")
    print("="*60)
    average_iterative = demonstrate_tail_recursion_conversion(books, "Robert C. Martin")
    
    # Verify both give same result
    print(f"\nVerification: Recursive = {average_weight:.2f} Kg, "
          f"Iterative = {average_iterative:.2f} Kg")
    print(f"Results match: {abs(average_weight - average_iterative) < 0.01}")
