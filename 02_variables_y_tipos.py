# 02_variables_y_tipos.py
# Módulo 2.1: Variables y tipos de datos

# Tipos de datos primitivos en Python
entero = 25              # int
decimal = 3.1416         # float
texto = "Monse"          # str
es_estudiante = True     # bool

print(f"Entero: {entero} -> Tipo: {type(entero)}")
print(f"Decimal: {decimal} -> Tipo: {type(decimal)}")
print(f"Texto: {texto} -> Tipo: {type(texto)}")
print(f"Booleano: {es_estudiante} -> Tipo: {type(es_estudiante)}")

# Conversión de tipos (Casting)
numero_texto = "50"
numero_entero = int(numero_texto)
suma = numero_entero + 10
print(f"\nConversión de '{numero_texto}' a entero + 10 = {suma}")
