# 10_funciones_y_lambdas.py
# Módulo 5: Funciones, parámetros, retorno, lambda y ámbito (scope)

# Variable de ámbito global
empresa = "Santander Open Academy"

def calcular_area(base, altura=2):
    """
    Función documentada (docstring).
    Calcula el área de un rectángulo o paralelogramo.
    'base' y 'altura' son variables locales a la función.
    """
    area = base * altura
    return area

# Llamada a la función con argumento posicional y por defecto
resultado_area = calcular_area(5, 4)
print(f"Área (base=5, altura=4): {resultado_area}")
print(f"Área con altura por defecto (base=6): {calcular_area(6)}")

# Funciones lambda (funciones anónimas en una sola línea)
cuadrado = lambda x: x ** 2
print(f"\nFunción lambda cuadrado de 7: {cuadrado(7)}")

def mostrar_info():
    mensaje_local = "Python Básico"
    print(f"\nÁmbito local: {mensaje_local}")
    print(f"Ámbito global: {empresa}")

mostrar_info()
