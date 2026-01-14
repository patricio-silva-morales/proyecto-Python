numeros = [1, 4, 6, 3, 2, 6, 8]

# Forma eficiente
for elemento in numeros:
    print(elemento)

# Forma ineficiente
for i in range(len(numeros)):
    print(numeros[i])

# Forma eficiente
for i, elemento in enumerate(numeros):
    print(numeros[i])
    
