# Cadena a evaluar
cadena = "Primer ejemplo : ejemplo de conteo de frecuencia de palabras"

# Creamos el diccionario vacío
diccionario = {}

# Separa cada palabra de la cadena
for palabra in cadena.split():
    # Suma la ocurrencia de la palabra en el diccionario.
    # Si la clave no existe, primero la crea.
    diccionario[palabra] = diccionario.get(palabra, 0) + 1 
    
# Muestra el diccionario
print(diccionario)