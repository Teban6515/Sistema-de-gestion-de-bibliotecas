

### Primera ejecución

main.py
```
================================================================================
                         LIBRARY MANAGEMENT SYSTEM
                     Universidad de Caldas - 2025
================================================================================

Loading system...
✅ Loaded 25 books from data/books.json
✅ Loaded 5 users from data/users.json
✅ Loaded loan history for 5 users from data/loans_history.json

✅ System ready!
   📚 Books: 25
   👤 Users: 5

================================================================================
                              MAIN MENU
================================================================================

📚 BOOK MANAGEMENT
   1. Book Operations (Add, Search, Update, Delete, List)

👤 USER MANAGEMENT
   2. User Operations (Add, Search, Update, Delete, List)

📖 LOAN MANAGEMENT
   3. Loan Operations (Loan Book, Return Book, View History)

🔬 ALGORITHMS & ANALYSIS
   4. Shelf Analysis (Brute Force & Backtracking)
   5. Recursive Functions (Stack & Tail Recursion)
   6. Generate Reports (Sorted by Value)

💾 SYSTEM
   7. Save All Data
   8. Create Backup
   9. Exit
================================================================================

👉 Select option:
```

### Navegación básica

1. **Selecciona una opción** escribiendo el número y presionando Enter
2. **Sigue las instrucciones** en pantalla
3. **Para regresar** a un menú anterior, selecciona la opción "Back"
4. **Para salir** del sistema, selecciona opción 9 en el menú principal

---

## 🧪 PASO 6: PROBAR LAS FUNCIONALIDADES

### Prueba 1: Ver los libros
```
Menú Principal → 1 → 3
(Book Management → List All Books)
```

Deberías ver los 25 libros cargados desde el archivo JSON.

### Prueba 2: Buscar un libro
```
Menú Principal → 1 → 2 → 2
(Book Management → Search Book → Search by Title)
```
Escribe: **Clean Code**

### Prueba 3: Ejecutar Brute Force
```
Menú Principal → 4 → 1
(Shelf Analysis → Brute Force)
```

Esto encuentra todas las combinaciones de 4 libros que superan 8 Kg.

### Prueba 4: Ejecutar Backtracking
```
Menú Principal → 4 → 2
(Shelf Analysis → Backtracking)
```

Esto encuentra la combinación óptima de libros que maximiza el valor sin exceder 8 Kg.

### Prueba 5: Recursión de Cola
```
Menú Principal → 5 → 2
(Recursive Functions → Tail Recursion)
```
Escribe un autor: **Robert C. Martin**

Verás la demostración paso a paso de la recursión de cola.


---

## 📊 ARCHIVOS GENERADOS

Durante el uso del sistema, se generarán reportes en la carpeta `reports/`:

- `risky_combinations.txt` - Combinaciones peligrosas (Brute Force)
- `optimal_shelf.txt` - Configuración óptima (Backtracking)
- `inventory_value_report.txt` - Reporte de inventario por valor

## 📚 RECURSOS ADICIONALES

- **Documentación Python**: https://docs.python.org/3/
- **VS Code Python Tutorial**: https://code.visualstudio.com/docs/python/python-tutorial
- **Estructura del proyecto**: Ver `README.md`
- **Análisis técnico**: Ver `GUIA_DESARROLLO.md`

---
