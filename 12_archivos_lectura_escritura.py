# 12_archivos_lectura_escritura.py
# Módulo 7: Entradas/Salidas y manejo de archivos con la instrucción 'with'

nombre_archivo = "registro_curso.txt"

print("--- 1. Escritura de archivo en modo 'w' ---")
# 'with' garantiza que el archivo se cierre automáticamente al terminar
with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write("Curso de Python - Santander Open Academy\n")
    f.write("Estudiante: Monse\n")
    f.write("Estado: Aprobado con 10/10\n")
print(f"Archivo '{nombre_archivo}' creado y cerrado exitosamente.")

print("\n--- 2. Anexar contenido en modo 'a' (append) ---")
with open(nombre_archivo, "a", encoding="utf-8") as f:
    f.write("Fecha de finalización: Octubre 2026\n")
print("Línea adicional agregada.")

print("\n--- 3. Lectura del archivo en modo 'r' ---")
with open(nombre_archivo, "r", encoding="utf-8") as f:
    contenido = f.read()

print("Contenido leído del archivo:")
print("----------------------------")
print(contenido)
