frase = input("Ingrese una frase: ")

# CReamos una lista con las palabras de la frase
palabras = frase.split()

# print(palabras)
# print(type(palabras))

# Creamos el diccionario vacío
frecuencia = {}

# El diccionario contendrá las ocurrencias por palabra
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
# Creamos una lista con la frecuencia de las palabras
salida = list(frecuencia.items())
# Ordenamos descendentemente la lista
salida.sort(reverse = True)
# Mostramos la lista
print(salida)