import fcntl

archivo = None

try:
    # Abro el archivo
    archivo = open("/home/tu_usuario/archivo_seguro.txt", "r", encoding="utf-8")

    # Bloqueo exclusivo (equivalente conceptual a LK_LOCK)
    fcntl.flock(archivo, fcntl.LOCK_EX)

    # Uso el archivo (está bloqueado para otros procesos que también usen flock)
    print(archivo.read())

except FileNotFoundError:
    print("El archivo no existe")

finally:
    if archivo is not None:
        # Desbloqueo
        fcntl.flock(archivo, fcntl.LOCK_UN)
        archivo.close()

    print("Gracias por utilizar la aplicación")
