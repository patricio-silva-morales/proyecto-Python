# Creamos el diccionario vacío
cuadrados = {}

# for i in range(10):
#     cuadrados[i] = i ** 2

# Usamos comprensión de diccionario para crear los elementos
cuadrados = { i: i ** 2 for i in range(10) }
    
print(cuadrados)