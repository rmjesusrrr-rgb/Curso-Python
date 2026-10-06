# Resumen Completo: Curso de Python (Santander Open Academy)

Este documento recopila la teoría, sintaxis, ejemplos prácticos y mejores prácticas de los 8 módulos del curso.

---

## Módulo 1: Introducción a Python
* **¿Qué es Python?**: Lenguaje de programación de alto nivel, interpretado, de tipado dinámico y sintaxis limpia.
* **Instalación y Entorno**: Se ejecuta mediante el intérprete de Python y herramientas como VS Code, IDLE o terminales.
* **Primer Programa**:
  ```python
  print("Hola Mundo")
  ```

---

## Módulo 2: Fundamentos de Python

### 2.1 Variables y Tipos de Datos
En Python no es necesario declarar el tipo de variable:
```python
entero = 10              # int
decimal = 3.14           # float
texto = "Python"         # str
booleano = True          # bool

# Conversión de tipos (Casting)
edad_str = "25"
edad_num = int(edad_str)
```

### 2.2 Operadores
* **Aritméticos**: `+`, `-`, `*`, `/` (división decimal), `//` (división entera), `%` (módulo/resto), `**` (potencia).
* **Comparación**: `==`, `!=`, `>`, `<`, `>=`, `<=`.
* **Lógicos**:
  - `and`: Verdadero si ambas condiciones son verdaderas.
  - `or`: Verdadero si al menos una condición es verdadera.
  - `not`: Invierte el valor de verdad.
  ```python
  # Ejemplo evaluado en el examen:
  resultado = (not True) or (False and True)  # False or False -> False
  ```

---

## Módulo 3: Estructuras de Control

### Condicionales
```python
numero = 7
if numero % 2 == 0:
    resultado = "Par"
else:
    resultado = "Impar"
```

### 3.1 Bucles (Loops)
* **Bucle `for`**: Ideal para iterar sobre secuencias (listas, tuplas, rangos).
  ```python
  for i in range(5):  # 0, 1, 2, 3, 4
      print(i)
  ```
* **Bucle `while`**: Se ejecuta mientras se cumpla una condición.
  ```python
  contador = 0
  while contador < 3:
      contador += 1
  ```
* **Control de flujo**:
  - `break`: Detiene el bucle por completo.
  - `continue`: Salta directamente a la siguiente iteración.

---

## Módulo 4: Estructuras de Datos

| Estructura | Sintaxis | Ordenada | Mutable | Elementos duplicados |
| :--- | :--- | :--- | :--- | :--- |
| **Lista** | `[1, 2, 3]` | Sí | **Sí** | Sí |
| **Tupla** | `(1, 2, 3)` | Sí | **No** (Inmutable) | Sí |
| **Diccionario** | `{"clave": "valor"}` | Sí (3.7+) | **Sí** | Claves únicas |
| **Conjunto (set)**| `{1, 2, 3}` | No | **Sí** (en agregado) | **No** (Únicos) |

### Métodos Clave:
```python
# Listas
frutas = ["manzana", "plátano"]
frutas.append("naranja")   # Agrega al final

# Tuplas (inmutables)
coordenadas = (10, 20)

# Diccionarios
alumno = {"nombre": "Monse", "curso": "Python"}
print(alumno["nombre"])

# Conjuntos (Set)
unicos = {1, 2, 2, 3}  # {1, 2, 3}
```

---

## Módulo 5: Funciones y Ámbito (Scope)
* Se definen con la palabra clave `def`.
* **Ámbito local vs global**:
  - Las variables **locales** solo existen dentro de la función donde se definieron.
  - Las variables **globales** se definen fuera y son accesibles en todo el archivo.

```python
x_global = 100

def sumar(a, b=0):
    resultado_local = a + b
    return resultado_local

# Funciones lambda (anónimas):
cuadrado = lambda x: x ** 2
```

---

## Módulo 6: Manejo de Errores y Excepciones
* Las excepciones gestionan fallos en tiempo de ejecución sin detener el programa inesperadamente.
* Bloque `try - except - else - finally`:

```python
try:
    numero = int("abc")  # Genera ValueError
except ValueError as e:
    print(f"Error detectado: {e}")
finally:
    print("Este bloque siempre se ejecuta.")

# Lanzar excepciones propias:
# raise ValueError("Mensaje de error")
```

---

## Módulo 7: Entradas, Salidas y Archivos
* Lectura por teclado: `nombre = input("Ingresa tu nombre: ")`
* Manejo seguro de archivos con la sentencia `with`:

```python
# Escritura ('w' sobrescribe, 'a' anexa)
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Línea 1\n")

# Lectura ('r')
with open("notas.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
```
> El uso de `with` garantiza que el archivo se cierre automáticamente al terminar el bloque, incluso si ocurre un error.

---

## Módulo 8: Módulos y Paquetes
* **Módulo**: Cualquier archivo con extensión `.py`.
* **Importación**:
  ```python
  import math
  from math import sqrt
  ```
* **Punto de entrada (`__name__ == '__main__'`)**:
  Permite que el código se ejecute cuando el archivo se lanza directamente, pero no cuando se importa como módulo.
* **Paquete**: Una carpeta que contiene módulos y típicamente un archivo `__init__.py`.

---

## Resultados y Respuestas de las Evaluaciones

### Control de Avance (Módulos 1 al 4) &mdash; Puntuación: 3 / 3 (100%)
1. `numero = 7` &rarr; `"Impar"`
2. Conteo de pares en `(4, 7, 10, 3, 8)` &rarr; `3`
3. Colección ordenada y mutable &rarr; `Lista`

### Autoevaluación Final (Módulos 1 al 8) &mdash; Puntuación: 10 / 10 (100%)
1. Capturar excepciones &rarr; `try`
2. Abrir archivo en modo escritura &rarr; `file = open("archivo.txt", "w")`
3. Agregar elemento al final de una lista &rarr; `append()`
4. Propósito principal de `append()` &rarr; Agregar un elemento al final de la lista
5. Sobre excepciones &rarr; Se utilizan para manejar errores y situaciones excepcionales
6. Variable local vs global &rarr; Las locales solo pueden ser accedidas dentro de una función
7. Propósito de `with` en archivos &rarr; Cerrar automáticamente el archivo después de su uso
8. Lógica `(not True) or (False and True)` &rarr; `False`
9. Diferencia tupla y lista &rarr; Las tuplas son inmutables, las listas son mutables
10. `x = 5; y = "3"; z = x + int(y)` &rarr; `8`
