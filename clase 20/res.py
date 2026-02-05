import os
import shutil

archivo = None

try:
    nombre = input("Nombre del archivo: ")
    contenido = input("Contenido: ")

    archivo = open(nombre, "w", encoding="utf-8")
    archivo.write(contenido)
    archivo.close()
    archivo = None

    os.makedirs("backup", exist_ok=True)
    shutil.move(nombre, "backup/" + nombre)

except FileNotFoundError:
    print("Archivo no encontrado")

except PermissionError:
    print("Permiso denegado")

finally:
    if archivo is not None:
        archivo.close()
    print("Proceso finalizado")
