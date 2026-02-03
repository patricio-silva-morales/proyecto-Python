import os # Necesario para usar os.stat()

try:
    nombre = input("Ingresa el nombre del archivo: ").strip()
    archivo = open(nombre, "r", encoding="utf-8") # Abre archivo para lectura

    print("Nombre:", archivo.name)
    print("Modo:", archivo.mode)
    print("Cerrado:", archivo.closed)

    # Obtiene el tamaño del archivo en bytes
    tamaño = os.stat(nombre).st_size
    print("Tamaño en bytes:", tamaño)

    if tamaño < 500:
        # Lee el contenido completo
        contenido = archivo.read()
        print(contenido)
    else:
        # Lee el contenido línea a línea
        linea = archivo.readline()
        while linea:
            print(linea, end="")
            linea = archivo.readline()

    archivo.close()
    print("\nCerrado:", archivo.closed)

except FileNotFoundError:
    print("El archivo no existe")