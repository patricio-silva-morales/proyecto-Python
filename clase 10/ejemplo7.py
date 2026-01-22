def cuadrado(x):
    return x ** 2

def mayor(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

numero = int(input("Ingrese un número: "))
print(cuadrado(numero))

numero1 = int(input("Ingrese un número 1: "))
numero2 = int(input("Ingrese un número 2: "))
numero3 = int(input("Ingrese un número 3: "))
print(mayor(numero1, numero2, numero3))