# 🚀 GUÍA DE DESARROLLO - PROYECTO BIBLIOTECA

## ✅ MÓDULOS COMPLETADOS

### 1. Modelos de Datos (100% completo)
- ✅ `src/models/book.py` - Clase Book con todos los atributos
- ✅ `src/models/user.py` - Clase User con gestión de préstamos
- ✅ `src/models/shelf.py` - Clase Shelf con capacidad de peso

### 2. Estructuras de Datos (100% completo)
- ✅ `src/data_structures/stack.py` - Pila (LIFO) para historial de préstamos
- ✅ `src/data_structures/queue.py` - Cola (FIFO) para reservas

### 3. Algoritmos de Ordenamiento (100% completo)
- ✅ `src/algorithms/sorting.py`:
  - Insertion Sort por ISBN
  - Merge Sort por Valor
  - Funciones auxiliares de mezcla

### 4. Algoritmos de Búsqueda (100% completo)
- ✅ `src/algorithms/searching.py`:
  - Linear Search por Título/Autor
  - Binary Search por ISBN (CRÍTICA)
  - Verificación de reservas pendientes

### 5. Recursividad (100% completo)
- ✅ `src/algorithms/recursion.py`:
  - Recursión de pila: valor total por autor
  - Recursión de cola: peso promedio por autor
  - Demostración de conversión a iterativo

### 6. Datos Iniciales (100% completo)
- ✅ `data/books.json` - 25 libros de programación
- ✅ `data/users.json` - 5 usuarios iniciales
- ✅ `data/loans_history.json` - Estructura para historial
- ✅ `data/reservations.json` - Estructura para reservas

### 7. Documentación (100% completo)
- ✅ `README.md` - Documentación completa en inglés
- ✅ Comentarios y docstrings en todos los módulos

---

## 📝 MÓDULOS FALTANTES (A COMPLETAR)

### 1. Problem Solving (PRIORITARIO)

#### `src/problem_solving/brute_force.py`
```python
"""
Implementar algoritmo de fuerza bruta para encontrar combinaciones 
de 4 libros que superen 8 Kg.
"""

from itertools import combinations

def find_risky_shelf_combinations(books_list, max_weight=8.0, combination_size=4):
    """
    Find all combinations of 4 books exceeding weight threshold.
    
    Uses brute force to exhaustively explore all possible combinations.
    
    Time Complexity: O(n^4) for combinations of 4
    """
    risky_combinations = []
    
    # Generate all combinations of 4 books
    for combo in combinations(books_list, combination_size):
        total_weight = sum(book.weight for book in combo)
        
        if total_weight > max_weight:
            risky_combinations.append({
                'books': combo,
                'total_weight': total_weight,
                'excess_weight': total_weight - max_weight
            })
    
    return risky_combinations
```

#### `src/problem_solving/backtracking.py`
```python
"""
Implementar backtracking para maximizar valor sin exceder 8 Kg.
"""

def find_optimal_shelf_backtracking(books_list, max_weight=8.0):
    """
    Find combination of books that maximizes value without exceeding weight.
    
    Uses backtracking with pruning for optimization.
    
    Args:
        books_list: List of Book objects
        max_weight: Maximum weight capacity (8 Kg)
    
    Returns:
        dict: Best combination with books, total_value, total_weight
    """
    best_solution = {
        'books': [],
        'total_value': 0,
        'total_weight': 0
    }
    
    def backtrack(index, current_books, current_weight, current_value):
        nonlocal best_solution
        
        # Update best solution if current is better
        if current_value > best_solution['total_value']:
            best_solution = {
                'books': current_books.copy(),
                'total_value': current_value,
                'total_weight': current_weight
            }
        
        # Base case: explored all books
        if index >= len(books_list):
            return
        
        # Try including current book
        book = books_list[index]
        if current_weight + book.weight <= max_weight:
            current_books.append(book)
            backtrack(index + 1, current_books, 
                     current_weight + book.weight,
                     current_value + book.value)
            current_books.pop()  # Backtrack
        
        # Try excluding current book
        backtrack(index + 1, current_books, current_weight, current_value)
    
    backtrack(0, [], 0, 0)
    return best_solution
```

### 2. Gestores del Sistema

#### `src/managers/inventory_manager.py`
```python
"""
Gestor principal del inventario con ambas listas.
"""

class InventoryManager:
    def __init__(self):
        self.general_inventory = []  # Unsorted list
        self.sorted_inventory = []   # Sorted by ISBN
    
    def add_book(self, book):
        """Add book to both inventories."""
        self.general_inventory.append(book)
        self.sorted_inventory.append(book)
        insertion_sort_by_isbn(self.sorted_inventory)
    
    def search_by_isbn(self, isbn):
        """Use binary search on sorted inventory."""
        return binary_search_by_isbn(self.sorted_inventory, isbn)
    
    def generate_value_report(self):
        """Generate report sorted by value using Merge Sort."""
        sorted_by_value = merge_sort_by_value(self.general_inventory.copy())
        return sorted_by_value
```

#### `src/managers/loan_manager.py`
```python
"""
Gestor de préstamos usando Stack para historial.
"""

class LoanManager:
    def __init__(self):
        self.loan_histories = {}  # user_id -> Stack
    
    def loan_book(self, user_id, isbn):
        """
        Loan a book to user.
        Adds to user's loan history stack.
        """
        if user_id not in self.loan_histories:
            self.loan_histories[user_id] = Stack()
        
        loan_record = {
            'isbn': isbn,
            'date': datetime.now().isoformat()
        }
        self.loan_histories[user_id].push(loan_record)
    
    def return_book(self, user_id, isbn):
        """
        Return a book.
        MUST check for pending reservations using binary search.
        """
        # Implementation here
        pass
```

#### `src/managers/user_manager.py`
```python
"""
Gestor de usuarios con CRUD completo.
"""

class UserManager:
    def __init__(self):
        self.users = {}  # user_id -> User
    
    def create_user(self, user):
        """Create new user."""
        self.users[user.user_id] = user
    
    def get_user(self, user_id):
        """Get user by ID."""
        return self.users.get(user_id)
    
    def update_user(self, user_id, **kwargs):
        """Update user information."""
        # Implementation
        pass
    
    def delete_user(self, user_id):
        """Delete user."""
        # Implementation
        pass
```

### 3. Utilidades

#### `src/utils/file_handler.py`
```python
"""
Manejo de archivos JSON para persistencia.
"""

import json

def load_books(filename='data/books.json'):
    """Load books from JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [Book.from_dict(b) for b in data['books']]

def save_books(books, filename='data/books.json'):
    """Save books to JSON file."""
    data = {'books': [b.to_dict() for b in books]}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
```

#### `src/utils/validators.py`
```python
"""
Validaciones de entrada.
"""

def validate_isbn(isbn):
    """Validate ISBN format."""
    return isinstance(isbn, str) and len(isbn) >= 10

def validate_email(email):
    """Validate email format."""
    return '@' in email and '.' in email
```

### 4. Main Application

#### `main.py`
```python
"""
Aplicación principal con menú interactivo.
"""

def main():
    print("="*50)
    print("  LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    
    while True:
        print("\n1. Book Management")
        print("2. User Management")
        print("3. Loan Management")
        print("4. Reservation Management")
        print("5. Shelf Analysis (Brute Force & Backtracking)")
        print("6. Generate Reports")
        print("7. Recursive Functions Demo")
        print("8. Exit")
        
        choice = input("\nSelect option: ")
        
        if choice == '1':
            book_management_menu()
        elif choice == '2':
            user_management_menu()
        # ... etc

if __name__ == "__main__":
    main()
```

---

## 🎯 PRÓXIMOS PASOS

### Paso 1: Completar Problem Solving
1. Crear `brute_force.py` con el algoritmo completo
2. Crear `backtracking.py` con optimización
3. Probar ambos con el inventario de 25 libros

### Paso 2: Crear Gestores
1. `inventory_manager.py` - Gestión de inventarios
2. `loan_manager.py` - Gestión de préstamos
3. `user_manager.py` - Gestión de usuarios

### Paso 3: Implementar Utilidades
1. `file_handler.py` - Carga/guardado de datos
2. `validators.py` - Validaciones

### Paso 4: Main Application
1. Crear menú principal interactivo
2. Integrar todos los módulos
3. Implementar CRUD para todas las entidades

### Paso 5: Testing
1. Probar cada algoritmo individualmente
2. Probar flujos completos (préstamo → devolución → reserva)
3. Verificar persistencia de datos

### Paso 6: Documentación Final
1. Completar README con screenshots
2. Crear video de demostración
3. Preparar informe técnico

---

## 📚 ESTRUCTURA ACTUAL DEL PROYECTO

```
LibraryManagementSystem/
├── README.md                        ✅ Completo
├── requirements.txt                 ✅ Completo
├── data/
│   ├── books.json                   ✅ 25 libros
│   ├── users.json                   ✅ 5 usuarios
│   ├── loans_history.json           ✅ Estructura
│   └── reservations.json            ✅ Estructura
├── src/
│   ├── models/                      ✅ 100% completo
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── user.py
│   │   └── shelf.py
│   ├── data_structures/             ✅ 100% completo
│   │   ├── __init__.py
│   │   ├── stack.py
│   │   └── queue.py
│   ├── algorithms/                  ✅ 100% completo
│   │   ├── __init__.py
│   │   ├── sorting.py
│   │   ├── searching.py
│   │   └── recursion.py
│   ├── problem_solving/             ⏳ FALTA
│   │   ├── __init__.py
│   │   ├── brute_force.py           ❌ Por crear
│   │   └── backtracking.py          ❌ Por crear
│   ├── managers/                    ⏳ FALTA
│   │   ├── __init__.py
│   │   ├── inventory_manager.py     ❌ Por crear
│   │   ├── loan_manager.py          ❌ Por crear
│   │   └── user_manager.py          ❌ Por crear
│   └── utils/                       ⏳ FALTA
│       ├── __init__.py
│       ├── file_handler.py          ❌ Por crear
│       └── validators.py            ❌ Por crear
├── main.py                          ❌ Por crear
└── reports/                         ✅ Carpeta creada
```

---

## 💡 CONSEJOS DE IMPLEMENTACIÓN

### Para Brute Force:
- Usa `itertools.combinations` para generar combinaciones
- Itera todas las combinaciones de 4 libros
- Filtra las que superen 8 Kg
- Retorna lista ordenada por peso excedente

### Para Backtracking:
- Usa función recursiva con parámetros de estado
- Implementa poda: si peso actual + peso mínimo restante > 8, retorna
- Mantén variable global con mejor solución
- Explora ambas opciones: incluir/excluir cada libro

### Para Gestores:
- Usa composición: cada gestor tiene instancias de las estructuras
- Separa lógica de negocio de presentación
- Implementa métodos claros y bien documentados
- Maneja excepciones apropiadamente

---

## 📞 SOPORTE

Si tienes dudas:
1. Revisa el README.md completo
2. Consulta los docstrings en cada módulo
3. Ejecuta los tests al final de cada archivo
4. Revisa los ejemplos de uso

---

**Fecha:** Diciembre 2025  
**Versión:** 1.0 (Base completa - 60% del proyecto)  
**Progreso:** 
- ✅ Fundamentos: 100%
- ✅ Algoritmos Core: 100%
- ⏳ Integración: 40%
- ⏳ UI/UX: 0%
