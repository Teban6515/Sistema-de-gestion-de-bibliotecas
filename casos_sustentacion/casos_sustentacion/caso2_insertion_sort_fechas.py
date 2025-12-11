
from datetime import datetime


def insertion_sort_loans_by_date(loan_history_stack):

    # Convert Stack to list for sorting
    loans_list = loan_history_stack.items.copy()
    
    print("\n" + "="*80)
    print("INSERTION SORT: Loan History by Date")
    print("="*80)
    print(f"\nOriginal order ({len(loans_list)} loans):")
    for i, loan in enumerate(loans_list):
        print(f"  [{i}] {loan['loan_date'][:10]} - {loan['title'][:40]}")
    
    # INSERTION SORT ALGORITHM
    comparisons = 0
    swaps = 0
    
    for i in range(1, len(loans_list)):
        key_loan = loans_list[i]
        key_date = datetime.fromisoformat(key_loan['loan_date'])
        j = i - 1
        
        print(f"\n--- Pass {i}: Inserting loan from {key_loan['loan_date'][:10]} ---")
        
        # Move elements that have later dates to the right
        while j >= 0:
            comparisons += 1
            current_date = datetime.fromisoformat(loans_list[j]['loan_date'])
            
            if current_date > key_date:
                print(f"  Shifting: {loans_list[j]['loan_date'][:10]} > {key_date.date()}")
                loans_list[j + 1] = loans_list[j]
                swaps += 1
                j -= 1
            else:
                break
        
        # Insert the key loan in its correct position
        loans_list[j + 1] = key_loan
        print(f"  Inserted at position {j + 1}")
    
    print(f"\n📊 Algorithm Statistics:")
    print(f"   Total comparisons: {comparisons}")
    print(f"   Total shifts: {swaps}")
    
    print(f"\n✅ Sorted order (oldest to newest):")
    for i, loan in enumerate(loans_list):
        status = "✓" if loan.get('returned', False) else "✗"
        print(f"  [{i}] {loan['loan_date'][:10]} - {loan['title'][:40]} [{status}]")
    
    return loans_list

