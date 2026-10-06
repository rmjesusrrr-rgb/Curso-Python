# 09_diccionarios.py
# Módulo 4.2: Diccionarios (Estructuras clave - valor)

# Definición de un diccionario
estudiante = {
    "nombre": "Monse",
    "curso": "Python",
    "calificacion": 10.0,
    "activo": True
}

print(f"Diccionario completo:\n{estudiante}\n")

# Acceso a valores mediante claves
print(f"Nombre del estudiante: {estudiante['nombre']}")
print(f"Curso inscrito: {estudiante.get('curso')}")

# Agregar una nueva clave y modificar una existente
estudiante["edad"] = 22
estudiante["calificacion"] = 10.0
print(f"\nDiccionario actualizado con edad:\n{estudiante}\n")

# Iterar sobre las claves y valores
print("--- Claves y valores del diccionario ---")
for clave, valor in estudiante.items():
    print(f"- {clave}: {valor}")
