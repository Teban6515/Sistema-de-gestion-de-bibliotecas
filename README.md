# 📚 Library Management System (LMS)

## Project Overview

A comprehensive **Library Management System** developed in Python that demonstrates the implementation of fundamental programming techniques including data structures, sorting algorithms, searching algorithms, recursion, brute force, and backtracking.

**Course:** Programming Techniques  
**Institution:** Universidad de Caldas  
**Academic Period:** 2025-2  
**Developers:** [Your Names Here]

---

## 🎯 Project Objectives

This system demonstrates mastery of the following concepts:

- **Data Structures:** Lists, Stacks (LIFO), Queues (FIFO)
- **Sorting Algorithms:** Insertion Sort, Merge Sort
- **Searching Algorithms:** Linear Search, Binary Search
- **Problem Solving:** Brute Force, Backtracking
- **Recursion:** Stack Recursion, Tail Recursion
- **Object-Oriented Programming:** Classes, Encapsulation, Modularity
- **File Management:** JSON/CSV data persistence

---

## 📁 Project Structure

```
LibraryManagementSystem/
│
├── data/                          # Data files
│   ├── books.json                 # Initial inventory (20+ books)
│   ├── users.json                 # System users
│   ├── loans_history.json         # Loan history (Stack)
│   └── reservations.json          # Book reservations (Queue)
│
├── src/                           # Source code
│   ├── models/                    # Domain models
│   │   ├── book.py                # Book class
│   │   ├── user.py                # User class
│   │   └── shelf.py               # Shelf class
│   │
│   ├── data_structures/           # Data structures
│   │   ├── stack.py               # Stack (LIFO) implementation
│   │   └── queue.py               # Queue (FIFO) implementation
│   │
│   ├── algorithms/                # Algorithms
│   │   ├── sorting.py             # Insertion Sort, Merge Sort
│   │   ├── searching.py           # Linear Search, Binary Search
│   │   └── recursion.py           # Recursive functions
│   │
│   ├── problem_solving/           # Problem-solving algorithms
│   │   ├── brute_force.py         # Deficient shelf (brute force)
│   │   └── backtracking.py        # Optimal shelf (backtracking)
│   │
│   ├── managers/                  # System managers
│   │   ├── inventory_manager.py   # Inventory management
│   │   ├── loan_manager.py        # Loan management
│   │   └── user_manager.py        # User management
│   │
│   └── utils/                     # Utilities
│       ├── file_handler.py        # File I/O operations
│       └── validators.py          # Input validation
│
├── main.py                        # Main entry point
├── README.md                      # This file
├── requirements.txt               # Python dependencies
└── reports/                       # Generated reports
    └── inventory_report.txt
```

---

## 🚀 Features

### 1. Data Acquisition and Structures

#### 1.1 Data Loading
- Load initial inventory from JSON/CSV file
- Minimum 5 attributes per book: ISBN, Title, Author, Weight (Kg), Value (COP)
- Support for additional custom attributes

#### 1.2 List Management
- **General Inventory:** Unsorted list reflecting load order
- **Sorted Inventory:** Always maintained in ascending order by ISBN

#### 1.3 Stack (Loan History)
- LIFO (Last In, First Out) structure
- Tracks loan history per user
- Stores ISBN and loan date
- Persistent storage in file

#### 1.4 Queue (Reservations)
- FIFO (First In, First Out) structure
- Manages waiting list for out-of-stock books
- Only allows reservation when stock = 0
- Persistent storage in file

### 2. Sorting Algorithms

#### 2.1 Insertion Sort
- **Purpose:** Maintain Sorted Inventory
- **Trigger:** Every time a new book is added
- **Complexity:** O(n²) worst case, O(n) best case
- **Stability:** Stable sorting

#### 2.2 Merge Sort
- **Purpose:** Generate global inventory report by Value (COP)
- **Complexity:** O(n log n)
- **Stability:** Stable sorting
- **Output:** Report file with sorted inventory

### 3. Searching Algorithms

#### 3.1 Linear Search
- **Target:** General Inventory (unsorted list)
- **Search by:** Title or Author
- **Complexity:** O(n)
- **Use case:** Flexible attribute search

#### 3.2 Binary Search (Critical)
- **Target:** Sorted Inventory
- **Search by:** ISBN
- **Complexity:** O(log n)
- **Critical use:** Verify pending reservations on book return

### 4. Shelf Module: Problem-Solving Algorithms

#### 4.1 Brute Force (Deficient Shelf)
- **Objective:** Find all combinations of 4 books exceeding 8 Kg
- **Method:** Exhaustive exploration of all combinations
- **Complexity:** O(n⁴) for combinations of 4
- **Output:** List of all risky combinations

#### 4.2 Backtracking (Optimal Shelf)
- **Objective:** Maximize total value (COP) without exceeding 8 Kg capacity
- **Method:** Systematic exploration with pruning
- **Constraint:** Maximum weight = 8 Kg
- **Output:** Optimal book combination with maximum value

### 5. Recursion

#### 5.1 Stack Recursion
- **Function:** Calculate total value of all books by specific author
- **Type:** Traditional recursion
- **Complexity:** O(n)

#### 5.2 Tail Recursion
- **Function:** Calculate average weight of books by author
- **Type:** Tail-call optimized recursion
- **Output:** Console demonstration of tail recursion logic

---

## 💻 Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Visual Studio Code (recommended)
- Python extension for VS Code

### Installation Steps

1. **Clone or download the project:**
```bash
cd /path/to/your/workspace
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Verify data files exist:**
```bash
ls data/
# Should show: books.json, users.json, loans_history.json, reservations.json
```

4. **Run the system:**
```bash
python main.py
```

---

## 📖 Usage Guide

### Main Menu Options

```
========================================
  LIBRARY MANAGEMENT SYSTEM
========================================
1. Book Management
2. User Management
3. Loan Management
4. Reservation Management
5. Shelf Management (Algorithms)
6. Generate Reports
7. Exit
========================================
```

### Book Management
- Add new book (automatically updates Sorted Inventory)
- Search book (by ISBN, Title, or Author)
- Update book information
- Delete book
- List all books

### Loan Management
- Loan a book (adds to user's loan history stack)
- Return a book (checks for pending reservations)
- View loan history
- Calculate fines

### Shelf Management
- Run Brute Force algorithm (find risky combinations)
- Run Backtracking algorithm (optimal shelf configuration)
- View shelf statistics

### Reports
- Generate inventory report sorted by Value
- Export to file
- View statistics

---

## 🔧 Technical Implementation Details

### Key Algorithms Implementation

#### Insertion Sort (for Sorted Inventory)
```python
def insertion_sort_by_isbn(books_list):
    """
    Maintains sorted inventory by ISBN using insertion sort.
    Time Complexity: O(n²) worst case, O(n) best case
    Space Complexity: O(1)
    """
    for i in range(1, len(books_list)):
        key = books_list[i]
        j = i - 1
        while j >= 0 and books_list[j].isbn > key.isbn:
            books_list[j + 1] = books_list[j]
            j -= 1
        books_list[j + 1] = key
```

#### Binary Search (Critical for Reservations)
```python
def binary_search_isbn(sorted_books, isbn):
    """
    Searches for book by ISBN in sorted inventory.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Returns: index if found, -1 if not found
    """
    left, right = 0, len(sorted_books) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_books[mid].isbn == isbn:
            return mid
        elif sorted_books[mid].isbn < isbn:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

### Data Persistence

All data is stored in JSON format for easy reading and portability:

**books.json structure:**
```json
{
  "books": [
    {
      "isbn": "978-0-13-468599-1",
      "title": "Clean Code",
      "author": "Robert C. Martin",
      "weight": 0.8,
      "value": 125000,
      "stock": 3
    }
  ]
}
```

---

## 📊 Data Model

### Book Class
```python
class Book:
    """
    Represents a book in the library inventory.
    
    Attributes:
        isbn (str): International Standard Book Number (unique identifier)
        title (str): Book title
        author (str): Book author
        weight (float): Book weight in kilograms
        value (int): Book value in Colombian pesos (COP)
        stock (int): Number of copies available
    """
```

### User Class
```python
class User:
    """
    Represents a library user.
    
    Attributes:
        user_id (str): Unique user identifier
        name (str): User's full name
        email (str): User's email address
        loan_history (Stack): Stack of loan records (LIFO)
    """
```

### Shelf Class
```python
class Shelf:
    """
    Represents a physical shelf in the library.
    
    Attributes:
        shelf_id (str): Unique shelf identifier
        max_weight (float): Maximum weight capacity (8 Kg)
        books (list): List of books on this shelf
    """
```

---

## 🧪 Testing

### Test Cases

#### 1. Insertion Sort Test
- **Input:** Unsorted list of books
- **Expected:** Books sorted by ISBN in ascending order
- **Verification:** Compare ISBNs sequentially

#### 2. Binary Search Test
- **Input:** ISBN "978-0-13-468599-1"
- **Expected:** Return book position or -1
- **Verification:** Check returned index

#### 3. Brute Force Test
- **Input:** Inventory with 20 books
- **Expected:** All combinations of 4 books > 8 Kg
- **Verification:** Manually check some combinations

#### 4. Backtracking Test
- **Input:** Books with various weights and values
- **Expected:** Maximum value combination ≤ 8 Kg
- **Verification:** Compare with brute force result

---

## 📈 Performance Analysis

| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| Insertion Sort | O(n²) | O(1) | Small datasets, nearly sorted |
| Merge Sort | O(n log n) | O(n) | Large datasets, stable sorting |
| Linear Search | O(n) | O(1) | Unsorted data, flexible search |
| Binary Search | O(log n) | O(1) | Sorted data, fast retrieval |
| Brute Force (4 books) | O(n⁴) | O(1) | Small n, find all solutions |
| Backtracking | O(2ⁿ) | O(n) | Optimization with pruning |
| Stack Operations | O(1) | O(n) | LIFO access pattern |
| Queue Operations | O(1) | O(n) | FIFO access pattern |

---

## 🎥 Demo Video

[Link to demonstration video will be added here]

The video demonstrates:
1. System startup and data loading
2. CRUD operations for each entity
3. Loan and return workflow
4. Reservation queue management
5. Brute force and backtracking algorithms
6. Report generation
7. Code walkthrough

---

## 📝 Design Decisions and Justifications

### Why Two Inventory Lists?
- **General Inventory:** Preserves insertion order for audit purposes
- **Sorted Inventory:** Enables O(log n) binary search for critical operations

### Why Insertion Sort for Sorted Inventory?
- Efficient for small incremental additions (O(n) best case)
- Stable sorting preserves relative order
- In-place algorithm saves memory

### Why Merge Sort for Reports?
- Guaranteed O(n log n) performance
- Stable sorting maintains data integrity
- Suitable for large datasets

### Why Stack for Loan History?
- LIFO pattern matches real-world history access
- Recent loans are most relevant
- Efficient push/pop operations

### Why Queue for Reservations?
- FIFO ensures fairness (first come, first served)
- Natural model for waiting lists
- Simple implementation

---

## 👥 Authors

- **[Student Name 1]** - [Student ID]
- **[Student Name 2]** - [Student ID]

**Instructor:** [Professor Name]  
**Course:** Programming Techniques  
**Universidad de Caldas** - 2025-2

---

## 📄 License

This project is developed for academic purposes as part of the Programming Techniques course at Universidad de Caldas.

---

## 🙏 Acknowledgments

- Universidad de Caldas Faculty of Artificial Intelligence and Engineering
- Programming Techniques course materials and resources
- Python community for excellent documentation

---

## 📞 Contact

For questions or clarifications about this project:
- Email: [your.email@example.com]
- GitHub: [repository link]

---

**Last Updated:** December 2025  
**Version:** 1.0.0
