import os

try:
    nombre_archivo_1 = input("Archivo 1: ")
    nombre_archivo_2 = input("Archivo 2: ")

    archivo_1 = open(nombre_archivo_1, "r")
    archivo_2 = open(nombre_archivo_2, "r")

    tamaño_archivo_1 = os.stat(nombre_archivo_1).st_size
    tamaño_archivo_2 = os.stat(nombre_archivo_2).st_size

    lineas_archivo_1 = len(archivo_1.readlines())
    lineas_archivo_2 = len(archivo_2.readlines())

    print("Tamaño archivo 1:", tamaño_archivo_1)
    print("Tamaño archivo 2:", tamaño_archivo_2)
    print("Líneas archivo 1:", lineas_archivo_1)
    print("Líneas archivo 2:", lineas_archivo_2)

    if tamaño_archivo_1 > tamaño_archivo_2:
        print("El archivo 1 es más grande")
    elif tamaño_archivo_2 > tamaño_archivo_1:
        print("El archivo 2 es más grande")
    else:
        print("Ambos archivos tienen el mismo tamaño")

    if lineas_archivo_1 > lineas_archivo_2:
        print("El archivo 1 tiene más líneas")
    elif lineas_archivo_2 > lineas_archivo_1:
        print("El archivo 2 tiene más líneas")
    else:
        print("Ambos archivos tienen la misma cantidad de líneas")

    archivo_1.close()
    archivo_2.close()

except FileNotFoundError:
    print("Uno de los archivos no existe")