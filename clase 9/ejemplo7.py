def numeros(n):
    for i in range(n):
        yield i
    
# Creamos un GENERADOR    
g = numeros(5)

for x in g:
    print(x)
