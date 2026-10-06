# 08_tuplas_y_conjuntos.py
# Módulos 4.1 y 4.3: Tuplas (inmutables) y Conjuntos/Sets (elementos únicos)

print("--- TUPLAS (Ordenadas e inmutables) ---")
coordenadas = (19.4326, -99.1332)
print(f"Tupla: {coordenadas}")
print(f"Latitud: {coordenadas[0]}, Longitud: {coordenadas[1]}")
# Nota: coordenadas[0] = 20.0 generaría TypeError porque las tuplas no pueden modificarse.

print("\n--- CONJUNTOS / SETS (Desordenados, elementos no repetidos) ---")
numeros_con_duplicados = [1, 2, 2, 3, 4, 4, 4, 5]
conjunto_unicos = set(numeros_con_duplicados)
print(f"Lista original: {numeros_con_duplicados}")
print(f"Conjunto sin duplicados: {conjunto_unicos}")

# Operaciones de conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
print(f"Unión: {conjunto_a | conjunto_b}")
print(f"Intersección: {conjunto_a & conjunto_b}")
