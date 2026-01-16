def ingresar():
    return int(input("Ingrese un valor: "))
    
cuadrado_opt = [ingresar() for i in range(5)]

print(cuadrado_opt)