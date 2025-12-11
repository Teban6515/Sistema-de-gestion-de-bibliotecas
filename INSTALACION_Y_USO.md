# 🚀 GUÍA DE INSTALACIÓN Y EJECUCIÓN
## Sistema de Gestión de Bibliotecas - Universidad de Caldas

---

## 📋 REQUISITOS PREVIOS

### Software necesario:
1. **Python 3.8 o superior** ✅
   - Verificar: `python --version` o `python3 --version`
   - Descargar: https://www.python.org/downloads/

2. **Visual Studio Code** ✅
   - Descargar: https://code.visualstudio.com/

3. **Extensión de Python para VS Code** ✅
   - Se instala desde VS Code (ver pasos abajo)

---

## 📂 PASO 1: DESCARGAR Y EXTRAER EL PROYECTO

1. Descarga el proyecto desde el enlace proporcionado
2. Extrae el archivo ZIP en una ubicación de tu preferencia
3. Deberías ver una carpeta llamada `LibraryManagementSystem`

**Estructura del proyecto:**
```
LibraryManagementSystem/
├── main.py                    ← Archivo principal
├── README.md                  
├── requirements.txt           
├── data/                      ← Datos iniciales (25 libros, 5 usuarios)
├── src/                       ← Código fuente
└── reports/                   ← Reportes generados
```

---

## 🔧 PASO 2: CONFIGURAR VISUAL STUDIO CODE

### 2.1 Abrir el proyecto en VS Code

**Opción A - Desde VS Code:**
1. Abre Visual Studio Code
2. Click en "File" → "Open Folder..."
3. Navega hasta la carpeta `LibraryManagementSystem`
4. Click en "Seleccionar carpeta"

**Opción B - Desde la terminal:**
```bash
cd /ruta/a/LibraryManagementSystem
code .
```

### 2.2 Instalar la extensión de Python

1. En VS Code, presiona `Ctrl+Shift+X` (o `Cmd+Shift+X` en Mac)
2. En el buscador, escribe: **Python**
3. Instala la extensión oficial de Microsoft (debería ser la primera)
4. Espera a que se instale completamente

![Python Extension](https://code.visualstudio.com/assets/docs/languages/python/python-extension-marketplace.png)

### 2.3 Seleccionar el intérprete de Python

1. Presiona `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac)
2. Escribe: **Python: Select Interpreter**
3. Selecciona la versión de Python instalada en tu sistema

---

## 📦 PASO 3: INSTALAR DEPENDENCIAS

### 3.1 Abrir la terminal en VS Code

1. En VS Code, presiona `Ctrl+Ñ` (o menú: Terminal → New Terminal)
2. Deberías ver la terminal en la parte inferior

### 3.2 Verificar ubicación

Asegúrate de estar en la carpeta del proyecto:
```bash
# Deberías ver el contenido del proyecto
ls
# o en Windows:
dir
```

### 3.3 Instalar dependencias

```bash
# En Windows:
pip install -r requirements.txt

# En Mac/Linux:
pip3 install -r requirements.txt
```

**Si encuentras problemas:**
```bash
# Intenta con:
python -m pip install -r requirements.txt

# O con:
python3 -m pip install -r requirements.txt
```

---

## ▶️ PASO 4: EJECUTAR EL SISTEMA

### Método 1: Desde la terminal de VS Code

```bash
# En Windows:
python main.py

# En Mac/Linux:
python3 main.py
```

### Método 2: Usar el botón Play de VS Code

1. Abre el archivo `main.py` en VS Code
2. Verás un botón ▶️ (Play) en la esquina superior derecha
3. Click en el botón para ejecutar

---

## 🎯 PASO 5: USAR EL SISTEMA

### Primera ejecución

Al ejecutar `main.py`, verás:

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

## ⚠️ SOLUCIÓN DE PROBLEMAS COMUNES

### Problema 1: "Python no reconocido"

**Solución:**
1. Verifica que Python esté instalado: `python --version`
2. Agrega Python al PATH de tu sistema
3. Reinicia VS Code después de instalar Python

### Problema 2: "ModuleNotFoundError"

**Solución:**
```bash
pip install -r requirements.txt --upgrade
```

### Problema 3: "Permission denied"

**Solución en Mac/Linux:**
```bash
chmod +x main.py
python3 main.py
```

**Solución en Windows:**
- Ejecuta VS Code como administrador

### Problema 4: Error al cargar datos

**Solución:**
1. Verifica que la carpeta `data/` exista
2. Verifica que los archivos JSON estén presentes:
   - `data/books.json`
   - `data/users.json`
   - `data/loans_history.json`
   - `data/reservations.json`

### Problema 5: Encoding issues en Windows

Si ves caracteres raros (�), agrega al inicio de `main.py`:
```python
import sys
import os
# Agregar estas líneas
if os.name == 'nt':  # Si es Windows
    sys.stdout.reconfigure(encoding='utf-8')
```

---

## 💡 TIPS Y TRUCOS

### Atajos útiles en VS Code:

- `Ctrl+Ñ`: Abrir/cerrar terminal
- `Ctrl+B`: Mostrar/ocultar barra lateral
- `Ctrl+P`: Búsqueda rápida de archivos
- `F5`: Ejecutar en modo debug
- `Ctrl+Shift+P`: Paleta de comandos

### Para depurar el código:

1. Click en el número de línea para agregar un breakpoint (punto rojo)
2. Presiona `F5` para ejecutar en modo debug
3. El programa se detendrá en el breakpoint
4. Usa `F10` para avanzar línea por línea

### Ver la estructura del proyecto:

En la barra lateral izquierda (Explorer), puedes navegar por todas las carpetas y archivos.

---

## 📊 ARCHIVOS GENERADOS

Durante el uso del sistema, se generarán reportes en la carpeta `reports/`:

- `risky_combinations.txt` - Combinaciones peligrosas (Brute Force)
- `optimal_shelf.txt` - Configuración óptima (Backtracking)
- `inventory_value_report.txt` - Reporte de inventario por valor

---

## 🎥 PARA LA PRESENTACIÓN

### Grabar video de demostración:

1. **Windows**: Usa Xbox Game Bar (Win + G)
2. **Mac**: Usa QuickTime Player
3. **Multiplataforma**: OBS Studio (gratis)

### Qué mostrar en el video:

1. ✅ Ejecución del sistema
2. ✅ CRUD de libros
3. ✅ CRUD de usuarios
4. ✅ Flujo de préstamo y devolución
5. ✅ Búsqueda binaria en acción
6. ✅ Demostración de Brute Force
7. ✅ Demostración de Backtracking
8. ✅ Recursión de pila y cola
9. ✅ Generación de reportes

---

## 🔒 RESPALDO DE DATOS

### Crear backup manual:

```
Menú Principal → 8
(Create Backup)
```

Esto creará copias en `data/backups/` con timestamp.

### Guardar cambios:

```
Menú Principal → 7
(Save All Data)
```

Siempre guarda antes de cerrar el sistema.

---

## 📞 SOPORTE

Si encuentras problemas:

1. ✅ Revisa esta guía completamente
2. ✅ Verifica que Python esté correctamente instalado
3. ✅ Asegúrate de estar en la carpeta correcta del proyecto
4. ✅ Revisa que todos los archivos estén presentes
5. ✅ Intenta reiniciar VS Code

---

## ✅ CHECKLIST FINAL

Antes de la entrega/sustentación, verifica:

- [ ] Sistema ejecuta sin errores
- [ ] Puedes agregar libros (Insertion Sort funcionando)
- [ ] Puedes buscar por ISBN (Binary Search funcionando)
- [ ] Brute Force encuentra combinaciones peligrosas
- [ ] Backtracking encuentra solución óptima
- [ ] Recursión de pila calcula valor total
- [ ] Recursión de cola calcula promedio de peso
- [ ] Reportes se generan correctamente
- [ ] Datos se guardan y cargan correctamente
- [ ] Video de demostración grabado
- [ ] README.md completado
- [ ] Código documentado en inglés

---

## 🎓 INFORMACIÓN DEL PROYECTO

**Proyecto:** Sistema de Gestión de Bibliotecas  
**Curso:** Técnicas de Programación  
**Universidad:** Universidad de Caldas  
**Período:** 2025-2  
**Desarrollador:** Miguel Alejandro Bravo Ortiz

---

## 📚 RECURSOS ADICIONALES

- **Documentación Python**: https://docs.python.org/3/
- **VS Code Python Tutorial**: https://code.visualstudio.com/docs/python/python-tutorial
- **Estructura del proyecto**: Ver `README.md`
- **Análisis técnico**: Ver `GUIA_DESARROLLO.md`

---

**Última actualización:** Diciembre 2025  
**Versión del sistema:** 1.0 - Completo y Funcional

¡Buena suerte con tu presentación! 🚀
