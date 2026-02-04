import msvcrt
import os

try:
    
    # Abro el archivo
    archivo = open(r"C:\clon\proyecto-Python\clase 20\archivo_seguro.txt", "r")
    
    # Obtiene el tamaño (en bytes) del archivo
    tamaño = os.path.getsize(archivo.name) 
    
    # Bloqueo el archivo
    msvcrt.locking(archivo.fileno(), msvcrt.LK_LOCK, tamaño)
    
    # Uso el archivo (está bloqueado para otros procesos)
    print(archivo.read())
    
except FileNotFoundError:
    print("El archivo no existe")

else:    
    # Mueve el "cursor" al principio, tak como estaba al momento de bloquear
    archivo.seek(0)
    
    # Antes de cerrar, desbloqueo el archivo
    msvcrt.locking(archivo.fileno(), msvcrt.LK_UNLCK, tamaño)
    
    # Cierro el archivo
    archivo.close()
    
finally:
    print("Gracias por utilizar la aplicación")