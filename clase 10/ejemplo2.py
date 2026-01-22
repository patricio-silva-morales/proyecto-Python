def saludar():
    print("Hola!")
    
def multiplicar(a, b):
    return a * b

def bienvenida(nombre):
    saludar()
    return f"Bienvenida(o), {nombre}"

print(multiplicar(5, 4))
print(bienvenida("Cristina"))