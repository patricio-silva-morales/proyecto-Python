import os

# Problema corregido: La ruta relativa es la del  terminal, pero el
# archivo se encuentra en otra. La solución está en obtener la ruta
# del archivo y concatenarla
ruta = os.path.join(os.path.dirname(__file__), "info.txt")

try:
    archivo = open(ruta, "r")
    print(archivo.read())
    
except FileNotFoundError:
    print("Archivo no encontrado")
else:
    archivo.close()
finally:
    print("Cerrando recursos...")
    