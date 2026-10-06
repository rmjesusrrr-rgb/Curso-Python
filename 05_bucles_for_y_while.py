# 05_bucles_for_y_while.py
# Módulo 3.1: Bucles for y while

print("--- Bucle FOR iterando una lista ---")
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

print("\n--- Bucle FOR con range() ---")
for i in range(1, 6):
    print(f"Número: {i}")

print("\n--- Bucle WHILE con contador acumulativo ---")
contador = 0
while contador < 3:
    print(f"Contador en while: {contador}")
    contador += 1

print("\n--- Ejercicio del Examen: Contar pares en una tupla ---")
numeros = (4, 7, 10, 3, 8)
pares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
print(f"La tupla {numeros} tiene {pares} números pares.")
