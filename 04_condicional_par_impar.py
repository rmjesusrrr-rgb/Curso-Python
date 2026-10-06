# 04_condicional_par_impar.py
# Módulo 3: Estructuras de control condicionales (if / elif / else)

# Ejercicio evaluado en el examen
numero = 7

if numero % 2 == 0:
    resultado = "Par"
else:
    resultado = "Impar"

print(f"El número {numero} es: {resultado}")

# Ejemplo ampliado con elif:
calificacion = 85

if calificacion >= 90:
    nivel = "Excelente"
elif calificacion >= 70:
    nivel = "Aprobado"
else:
    nivel = "Reprobado"

print(f"Calificación {calificacion} -> Estado: {nivel}")
