import os

try:
    nombre = input("Archivo: ")
    f = open(nombre, "r")

    tamaño = os.stat(nombre).st_size
    
    # Leemos el archivo en una lista. Cada línea será un elemento
    lineas = f.readlines()
    
    total_caracteres = 0
    for l in lineas:
        total_caracteres += len(l)

    promedio = total_caracteres / len(lineas)

    print("Tamaño:", tamaño)
    print("Líneas:", len(lineas))
    print("Promedio caracteres por línea:", promedio)

    f.close()

except FileNotFoundError:
    print("El archivo no existe")