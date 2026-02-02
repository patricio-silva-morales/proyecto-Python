def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No puede dividir por cero")
            
    return a / b
    
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

try:
    print("El resultado de la división es ", dividir(numero1, numero2))
except ZeroDivisionError as e:
    print(e)