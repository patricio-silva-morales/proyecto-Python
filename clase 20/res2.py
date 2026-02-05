import os
import msvcrt

archivo = None

try:
    productos = []

    # Se leen los productos
    for i in range(2):
        nombre = input("Producto: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        productos.append(f"{nombre},{cantidad},{precio}\n")

    archivo = open("inventario.txt", "w")

    # Bloqueo
    msvcrt.locking(archivo.fileno(), msvcrt.LK_LOCK, 1)

    # Se registran los productos en el archivo
    archivo.writelines(productos)

    # Desbloqueo
    msvcrt.locking(archivo.fileno(), msvcrt.LK_UNLCK, 1)

    archivo.close()

    

    archivo = open("inventario.txt", "r")

    tamaño = os.path.getsize("inventario.txt")
    
    archivo.seek(0)
    
    # Bloqueo
    msvcrt.locking(archivo.fileno(), msvcrt.LK_LOCK, tamaño)

    print(archivo.read())

    archivo.seek(0)

    # Desbloqueo
    msvcrt.locking(archivo.fileno(), msvcrt.LK_UNLCK, tamaño)

    archivo.close()

except FileNotFoundError:
    print("No existe el archivo")
    
except PermissionError:
    print("No puede acceder al archivo")

finally:
    print("Proceso finalizado")
