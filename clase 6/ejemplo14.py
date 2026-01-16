numeros = [1, 4, 6, 3, 2, 6, 8]

# 1. Forma eficiente
for elemento in numeros:
    print(elemento)

# 2. Forma ineficiente
for i in range(len(numeros)):
    print(numeros[i])

# 3. Forma eficiente
for i, elemento in enumerate(numeros):
    print(numeros[i])