# 📂 CASOS DE SUSTENTACIÓN

Esta carpeta contiene las soluciones a los 4 posibles casos de modificación que el profesor puede solicitar durante la sustentación.

---

## 📋 CASOS DISPONIBLES

### CASO 1: Recursión Modificada
**Archivo:** `caso1_recursion_modificada.py`

**Requerimiento:**
> Modificar la función de Recursión de Pila para que encuentre y devuelva el ISBN del libro con el Peso más bajo de un autor.

**Ejecución:**
```bash
python caso1_recursion_modificada.py
```

**Qué Demuestra:**
- ✅ Recursión de pila (operaciones al retornar)
- ✅ Encuentra el libro más ligero correctamente
- ✅ Mantiene patrón recursivo del proyecto original

---

### CASO 2: Insertion Sort para Fechas
**Archivo:** `caso2_insertion_sort_fechas.py`

**Requerimiento:**
> Usar Insertion Sort para ordenar el Historial de Préstamos por fecha para un nuevo reporte.

**Ejecución:**
```bash
python caso2_insertion_sort_fechas.py
```

**Qué Demuestra:**
- ✅ Mismo algoritmo Insertion Sort
- ✅ Aplicado a fechas en vez de ISBN
- ✅ Genera reporte cronológico
- ✅ Muestra pasos del algoritmo

---

### CASO 3: Backtracking con Poda
**Archivo:** `caso3_backtracking_poda_peso.py`

**Requerimiento:**
> Agregar regla de poda que ignore libros con peso < 0.5 Kg al inicio de la llamada recursiva.

**Ejecución:**
```bash
python caso3_backtracking_poda_peso.py
```

**Qué Demuestra:**
- ✅ Nueva poda agregada al inicio
- ✅ Libros ligeros completamente ignorados
- ✅ Reduce espacio de búsqueda
- ✅ Compara eficiencia con/sin poda

---

### CASO 4: Cola → Pila
**Archivo:** `caso4_cola_a_pila.py`

**Requerimiento:**
> Invertir la lógica de reservas de Cola (FIFO) a Pila (LIFO).

**Ejecución:**
```bash
python caso4_cola_a_pila.py
```

**Qué Demuestra:**
- ✅ Operaciones renombradas (enqueue→push, dequeue→pop)
- ✅ Comportamiento LIFO funcionando
- ✅ Comparación visual con FIFO
- ✅ Estructura completa implementada

---

## 🚀 EJECUTAR TODOS LOS CASOS

Para ejecutar todos los casos en secuencia:

```bash
# Desde la raíz del proyecto:
python ejecutar_todos_los_casos.py
```

Este script:
- ✅ Ejecuta los 4 casos en orden
- ✅ Muestra resultados claramente
- ✅ Pausa entre cada caso
- ✅ Resume el estado al final

---

## 📖 CÓMO USAR DURANTE LA SUSTENTACIÓN

### Escenario 1: El profesor pide ver un caso específico

```bash
# Navegar a la carpeta
cd casos_sustentacion

# Ejecutar el caso solicitado
python caso1_recursion_modificada.py
python caso2_insertion_sort_fechas.py
python caso3_backtracking_poda_peso.py
python caso4_cola_a_pila.py
```

### Escenario 2: El profesor pide explicar cómo funciona

1. Abre el archivo en VS Code
2. Explica la modificación línea por línea
3. Ejecuta para demostrar funcionamiento
4. Compara con la versión original del proyecto

### Escenario 3: El profesor pide modificar en vivo

Usa los archivos como referencia y:
1. Abre el archivo correspondiente en el proyecto original
2. Explica qué cambiarías
3. Muestra el código ya preparado en casos_sustentacion
4. Ejecuta para demostrar que funciona

---

## 💡 TIPS PARA LA SUSTENTACIÓN

### Para CASO 1 (Recursión):
**Pregunta esperada:** "¿Cómo modificarías la recursión?"

**Respuesta:**
"Modifico la función para que retorne una tupla (isbn, weight) en vez de solo un valor. Durante el unwinding, comparo los pesos y retorno el ISBN del más ligero. Mantengo el patrón de recursión de pila porque las comparaciones ocurren al regresar de las llamadas recursivas."

### Para CASO 2 (Insertion Sort):
**Pregunta esperada:** "¿Cómo aplicarías Insertion Sort a fechas?"

**Respuesta:**
"El algoritmo es idéntico, solo cambio la comparación. En vez de comparar book.isbn, comparo datetime.fromisoformat(loan['date']). La estructura del algoritmo permanece: tomo un elemento, lo comparo con los anteriores, y lo inserto en su posición correcta."

### Para CASO 3 (Backtracking):
**Pregunta esperada:** "¿Cómo agregarías una nueva poda?"

**Respuesta:**
"Agrego la poda al inicio de la función recursiva, antes de cualquier otra verificación. Si book.weight < 0.5, incremento el contador de poda y llamo directamente a la siguiente iteración sin considerar este libro. Esto elimina ramas completas del árbol de búsqueda."

### Para CASO 4 (Cola → Pila):
**Pregunta esperada:** "¿Qué cambiaría de Cola a Pila?"

**Respuesta:**
"Cambio la estructura de datos de Queue a Stack. Renombro las operaciones: enqueue() → push(), dequeue() → pop(), front() → peek(). El comportamiento cambia de FIFO a LIFO: el último en reservar es el primero en obtener el libro. Mantengo la misma interfaz pero con semántica invertida."

---

## 📊 COMPARACIÓN DE CASOS

| Caso | Tipo | Dificultad | Tiempo Demo |
|------|------|------------|-------------|
| 1 | Recursión | Media | 2-3 min |
| 2 | Algoritmo | Fácil | 2-3 min |
| 3 | Optimización | Media | 3-4 min |
| 4 | Estructura | Fácil | 2-3 min |

---

## ✅ VERIFICACIÓN RÁPIDA

Antes de la sustentación, verifica que todos los casos funcionen:

```bash
# Test rápido
python caso1_recursion_modificada.py
python caso2_insertion_sort_fechas.py
python caso3_backtracking_poda_peso.py
python caso4_cola_a_pila.py
```

Si todos imprimen "✅ CASO X COMPLETADO" al final, estás listo.

---

## 🔧 TROUBLESHOOTING

### Error: "ModuleNotFoundError"
```bash
# Desde la raíz del proyecto:
pip install -r requirements.txt
```

### Error: "No module named 'src'"
```bash
# Asegúrate de ejecutar desde casos_sustentacion:
cd casos_sustentacion
python casoX_xxxxx.py
```

### Error: "FileNotFoundError" al cargar datos
```bash
# Los casos usan datos de prueba, no los archivos JSON
# Deberían funcionar sin necesitar data/
```

---

## 📚 RECURSOS ADICIONALES

- **GUIA_SUSTENTACION.md** - Guía completa de preparación
- **README.md** - Documentación técnica del proyecto
- **REFERENCIA_RAPIDA.md** - Comandos y atajos útiles

---

**Desarrollado por:** Miguel Alejandro Bravo Ortiz  
**Universidad:** Universidad de Caldas  
**Curso:** Técnicas de Programación  
**Fecha:** Diciembre 2025

¡Buena suerte en tu sustentación! 🚀
