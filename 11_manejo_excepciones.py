# 11_manejo_excepciones.py
# Módulo 6: Manejo de errores y excepciones (try / except / else / finally)

def division_segura(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        print(f"¡Error capturado!: No es posible dividir por cero ({e}).")
        return None
    except TypeError as e:
        print(f"¡Error de tipo capturado!: Ambos valores deben ser numéricos ({e}).")
        return None
    else:
        print("La operación se realizó exitosamente sin errores.")
        return resultado
    finally:
        print("Bloque FINALLY: este bloque se ejecuta siempre.")

print("--- Caso 1: División válida ---")
res1 = division_segura(10, 2)
print(f"Resultado: {res1}\n")

print("--- Caso 2: División entre cero ---")
res2 = division_segura(10, 0)
print(f"Resultado: {res2}\n")

# Creación de una excepción personalizada (Módulo 6.2)
class SaldoInsuficienteError(Exception):
    pass

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(f"No puedes retirar ${monto}, tu saldo es solo ${saldo}")
    return saldo - monto

try:
    print("--- Caso 3: Excepción personalizada ---")
    retirar(100, 250)
except SaldoInsuficienteError as error_personalizado:
    print(f"Excepción propia atrapada: {error_personalizado}")
