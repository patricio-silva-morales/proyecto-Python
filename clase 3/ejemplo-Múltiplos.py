numero = int(input("Ingrese un número: "))

if (numero % 2 == 0) and (numero % 3 == 0):
    print("El número es divisible por 2 y por 3")
elif numero % 2 == 0:
    print("El número es par solamente")
elif (numero % 2 == 1) and (numero % 3 == 0):
    print("El número es impar y múltiplo de 3")
    