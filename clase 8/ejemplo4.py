# Tupla de listas
tupla = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

# Mostramos la tupla
print(tupla)

# Modificamos el último elemento de cada lista de la tupla
for elemento in tupla:
    elemento[2] = 0
    
# Mostramos la tupla
print(tupla)

# Intentamos modificar la tupla: Error!!!
tupla[0] = [0, 0, 0]