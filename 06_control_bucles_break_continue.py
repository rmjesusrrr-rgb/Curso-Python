# 06_control_bucles_break_continue.py
# Módulo 3.1: Control de flujo en bucles con break y continue

print("--- Uso de BREAK (Detiene y sale del bucle) ---")
contador = 0
while True:
    print(f"Valor: {contador}")
    contador += 1
    if contador == 4:
        print("¡Se alcanzó 4, ejecutando break!")
        break

print("\n--- Uso de CONTINUE (Salta a la siguiente iteración) ---")
print("Imprimiendo solo los números impares del 0 al 9:")
for i in range(10):
    if i % 2 == 0:
        continue  # Salta los números pares
    print(f"Impar encontrado: {i}")
