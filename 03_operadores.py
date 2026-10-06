# 03_operadores.py
# Módulo 2.2: Operadores aritméticos, relacionales y lógicos

a = 10
b = 3

print("--- Operadores Aritméticos ---")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División decimal: {a} / {b} = {a / b:.2f}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Módulo (resto): {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

print("\n--- Operadores Relacionales ---")
print(f"¿{a} es mayor que {b}?: {a > b}")
print(f"¿{a} es igual a {b}?: {a == b}")

print("\n--- Operadores Lógicos (Pregunta del examen) ---")
expresion = (not True) or (False and True)
print(f"(not True) or (False and True) = {expresion}")
