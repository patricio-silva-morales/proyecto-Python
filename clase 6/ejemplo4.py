colores = ["blanco", "negro", "rojo", "azul", "amarillo", "verde", "naranjo", "morado", "café", "celeste"] #Lista a recorrer

# Enumerate recupera la posición del elemento
for i, color in enumerate(colores, start = 1): 
    print(i, color)
    
print("Cantidad de elementos: ", len(colores))