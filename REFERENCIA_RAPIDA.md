# ⚡ REFERENCIA RÁPIDA - SISTEMA DE BIBLIOTECAS

## 🚀 INICIO RÁPIDO

```bash
# 1. Navegar a la carpeta del proyecto
cd /ruta/a/LibraryManagementSystem

# 2. Ejecutar el sistema
python main.py       # Windows
python3 main.py      # Mac/Linux
```

---

## 📋 MENÚ PRINCIPAL

| Opción | Función | Algoritmo Usado |
|--------|---------|-----------------|
| 1 | Gestión de Libros | Linear Search, Binary Search |
| 2 | Gestión de Usuarios | CRUD básico |
| 3 | Gestión de Préstamos | Stack (LIFO) |
| 4 | Análisis de Estantes | Brute Force, Backtracking |
| 5 | Funciones Recursivas | Stack Recursion, Tail Recursion |
| 6 | Generar Reportes | Merge Sort |
| 7 | Guardar Datos | Persistencia JSON |
| 8 | Crear Backup | Backup automático |
| 9 | Salir | --- |

---

## 🎯 FLUJOS DE USO COMUNES

### Agregar un nuevo libro
```
Main Menu → 1 → 1
- Ingresar ISBN (ej: 978-0-13-468599-1)
- Ingresar título
- Ingresar autor
- Ingresar peso en Kg (ej: 0.8)
- Ingresar valor en COP (ej: 125000)
- Ingresar stock (ej: 3)
```
**Algoritmo:** Se agrega a inventario general Y se ordena con **Insertion Sort** en inventario ordenado.

### Buscar libro por ISBN
```
Main Menu → 1 → 2 → 1
- Ingresar ISBN
```
**Algoritmo:** **Binary Search** en O(log n) sobre inventario ordenado.

### Prestar un libro
```
Main Menu → 3 → 1
- Ingresar User ID
- Ingresar ISBN del libro
```
**Estructura:** Se agrega a **Stack** (LIFO) del historial del usuario.

### Devolver un libro
```
Main Menu → 3 → 2
- Ingresar User ID
- Ingresar ISBN del libro
```
**Algoritmo crítico:** Usa **Binary Search** para verificar reservas pendientes.

### Análisis de Fuerza Bruta
```
Main Menu → 4 → 1
```
**Algoritmo:** Prueba TODAS las combinaciones de 4 libros (C(n,4)) para encontrar las que superan 8 Kg.  
**Complejidad:** O(n⁴)

### Optimización con Backtracking
```
Main Menu → 4 → 2
- ¿Mostrar pasos? (y/n)
```
**Algoritmo:** Encuentra la combinación que maximiza valor sin exceder 8 Kg usando poda.  
**Complejidad:** O(2ⁿ) con poda eficiente

### Recursión de Pila
```
Main Menu → 5 → 1
- Ingresar nombre de autor (ej: Robert C. Martin)
```
**Función:** Calcula valor total de todos los libros del autor.  
**Tipo:** Recursión tradicional (operaciones en el retorno)

### Recursión de Cola
```
Main Menu → 5 → 2
- Ingresar nombre de autor
```
**Función:** Calcula peso promedio usando acumuladores.  
**Tipo:** Tail recursion (última operación es la llamada recursiva)

### Generar Reporte por Valor
```
Main Menu → 6 → 1
```
**Algoritmo:** **Merge Sort** ordena libros por valor en O(n log n).  
**Salida:** Lista descendente por valor + estadísticas

---

## 🔍 BÚSQUEDAS DISPONIBLES

### Por ISBN (Rápida)
- Usa **Binary Search** - O(log n)
- Requiere inventario ordenado
- Retorna libro exacto o null

### Por Título (Flexible)
- Usa **Linear Search** - O(n)
- Permite coincidencias parciales
- Retorna lista de coincidencias

### Por Autor (Flexible)
- Usa **Linear Search** - O(n)
- Permite coincidencias parciales
- Retorna todos los libros del autor

---

## 📊 COMPLEJIDADES IMPORTANTES

| Operación | Algoritmo | Complejidad | Notas |
|-----------|-----------|-------------|-------|
| Agregar libro | Insertion Sort | O(n²) peor, O(n) mejor | Eficiente para inserciones graduales |
| Buscar por ISBN | Binary Search | O(log n) | CRÍTICA - verifica reservas |
| Buscar por título/autor | Linear Search | O(n) | Para inventario desordenado |
| Reporte por valor | Merge Sort | O(n log n) | Garantiza rendimiento |
| Fuerza bruta 4 libros | Combinaciones | O(n⁴) | Exhaustivo |
| Backtracking | Búsqueda c/ poda | O(2ⁿ) | Con poda ~60-80% más rápido |
| Recursión pila | Recursión | O(n) tiempo, O(n) espacio | Call stack |
| Recursión cola | Recursión | O(n) tiempo, O(n) espacio | No optimizada en Python |

---

## 💾 PERSISTENCIA DE DATOS

### Archivos de datos:
```
data/
├── books.json              ← 25 libros iniciales
├── users.json              ← 5 usuarios iniciales
├── loans_history.json      ← Historial de préstamos (Stack)
└── reservations.json       ← Reservas pendientes (Queue)
```

### Comandos importantes:

**Guardar cambios:**
```
Main Menu → 7
```

**Crear backup:**
```
Main Menu → 8
```
Se guarda en `data/backups/` con timestamp.

---

## 🏗️ ESTRUCTURA DE CLASES PRINCIPAL

```
LibraryManagementSystem
├── InventoryManager
│   ├── general_inventory (lista desordenada)
│   └── sorted_inventory (ordenada por ISBN)
├── LoanManager
│   └── loan_histories (dict: user_id → Stack)
└── UserManager
    └── users (dict: user_id → User)
```

---

## 🔧 ATAJOS ÚTILES

### En el menú:
- Escribir número + Enter para seleccionar
- Presionar Enter sin escribir = mantener valor actual (en ediciones)
- Escribir 'n' para No, 'y' para Yes

### En la terminal:
- `Ctrl+C` = Interrumpir programa
- `Ctrl+Ñ` (VS Code) = Abrir/cerrar terminal
- Flecha arriba = Comando anterior

---

## ⚠️ CASOS ESPECIALES

### ISBN ya existe:
```
❌ Book with ISBN 978-xxx already exists!
```
**Solución:** Usa un ISBN diferente o actualiza el libro existente.

### Usuario sin préstamos activos:
```
❌ No loan history found
```
**Solución:** El usuario debe tener al menos un préstamo registrado.

### Libro sin stock:
```
❌ Book not available
```
**Solución:** Esperar devolución o verificar reservas.

### Límite de préstamos:
```
❌ User has reached maximum loans (5)
```
**Solución:** Usuario debe devolver libros antes de pedir más.

---

## 📈 ANÁLISIS DE RENDIMIENTO

### Inventario de 25 libros:

**Insertion Sort al agregar:**
- Mejor caso (ya ordenado): ~25 comparaciones
- Peor caso (inverso): ~312 comparaciones

**Binary Search por ISBN:**
- Máximo ~5 comparaciones (log₂ 25 ≈ 4.64)

**Brute Force (4 de 25):**
- Combinaciones: C(25,4) = 12,650
- Tiempo estimado: <0.1 segundos

**Backtracking (25 libros):**
- Nodos explorados: ~1,000-5,000 (con poda)
- Nodos totales posibles: 2²⁵ = 33,554,432
- Eficiencia: 99.98% de poda

---

## 🎓 PARA LA SUSTENTACIÓN

### Demuestra estos conceptos:

1. **Dos listas:**
   - General (desordenada, orden de carga)
   - Ordenada (por ISBN, con Insertion Sort)

2. **Insertion Sort:**
   - Agregar libro → automáticamente se ordena

3. **Binary Search (CRÍTICA):**
   - Buscar libro por ISBN
   - Verificar reservas al devolver

4. **Merge Sort:**
   - Generar reporte por valor

5. **Stack (LIFO):**
   - Historial de préstamos por usuario

6. **Queue (FIFO):**
   - Reservas de libros agotados

7. **Fuerza Bruta:**
   - Todas las combinaciones > 8 Kg

8. **Backtracking:**
   - Maximizar valor ≤ 8 Kg con poda

9. **Recursión de Pila:**
   - Valor total por autor

10. **Recursión de Cola:**
    - Peso promedio por autor

---

## ✅ CHECKLIST PRE-ENTREGA

- [ ] Sistema ejecuta sin errores
- [ ] Datos se cargan correctamente (25 libros, 5 usuarios)
- [ ] CRUD completo funciona (Create, Read, Update, Delete)
- [ ] Insertion Sort ordena al agregar libros
- [ ] Binary Search encuentra libros por ISBN
- [ ] Linear Search busca por título/autor
- [ ] Merge Sort genera reporte por valor
- [ ] Brute Force encuentra combinaciones >8Kg
- [ ] Backtracking optimiza estante ≤8Kg
- [ ] Recursión de pila calcula valor total
- [ ] Recursión de cola calcula peso promedio
- [ ] Stack gestiona historial de préstamos
- [ ] Guardar/cargar datos funciona
- [ ] Reportes se generan en /reports
- [ ] Código documentado en inglés
- [ ] README.md completo
- [ ] Video de demostración grabado

---

**Última actualización:** Diciembre 2025  
**Autor:** Miguel Bravo - Universidad de Caldas  
**Versión:** 1.0 - Sistema Completo
