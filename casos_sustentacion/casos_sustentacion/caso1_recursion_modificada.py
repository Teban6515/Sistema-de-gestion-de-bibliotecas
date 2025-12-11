

def find_lightest_book_isbn_by_author(books_list, author, index=0, lightest_book=None):

    # BASE CASE: Reached end of list
    if index >= len(books_list):
        return lightest_book.isbn if lightest_book else None
    
    current_book = books_list[index]
    
    # RECURSIVE CALL FIRST (builds the stack)
    result_from_rest = find_lightest_book_isbn_by_author(
        books_list, author, index + 1, lightest_book
    )
    
    # OPERATION DURING UNWINDING (stack recursion characteristic)
    # Check if current book is by the target author
    if current_book.author.lower() == author.lower():
        # Compare with lightest found in rest of list
        if result_from_rest is None:
            # This is the only book found so far
            return current_book.isbn
        else:
            # Find the book object with result_from_rest ISBN
            rest_lightest = next((b for b in books_list if b.isbn == result_from_rest), None)
            
            # Compare weights and return ISBN of lighter book
            if rest_lightest and current_book.weight < rest_lightest.weight:
                return current_book.isbn
            else:
                return result_from_rest
    
    # Current book not by target author, return result from rest
    return result_from_rest



