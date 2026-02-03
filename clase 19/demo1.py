try:

    print("Abriendo archivo...")
    
    archivo = open("c:\clon\prueba.txt", "r")   # Abre archivo en modo lectura

    contenido = archivo.read()                  # Lee el contenido y lo almacena
    
    print(f"Nombre del archivo: {archivo.name}")
    print(f"Modo de apertura: {archivo.mode}")

    print(contenido)                            # Muestra el contenido en la consola

except FileNotFoundError:
    print("El archivo no existe: No se pudo abrir el archivo")

else:
    if not archivo.closed:
        print("Cerrando archivo...")
        archivo.close                           # Cierra el archivo


    