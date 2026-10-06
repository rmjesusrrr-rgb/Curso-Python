# 07_listas_y_metodos.py
# Módulo 4: Listas en Python (Colecciones ordenadas y mutables)

# Creación de lista
colores = ["rojo", "verde", "azul"]
print(f"Lista inicial: {colores}")

# 1. append(): Agrega un elemento al final de la lista (Pregunta del examen)
colores.append("amarillo")
print(f"Después de append('amarillo'): {colores}")

# 2. insert(): Inserta en una posición específica
colores.insert(1, "naranja")
print(f"Después de insert(1, 'naranja'): {colores}")

# 3. Acceso por índice y mutabilidad
print(f"Primer elemento (índice 0): {colores[0]}")
colores[0] = "carmesí"
print(f"Modificando el índice 0: {colores}")

# 4. Longitud de la lista
print(f"Total de elementos: {len(colores)}")
