def sumar():
    numero1 = int(input("Ingrese el primer valor: "))
    numero2 = int(input("Ingrese el segundo valor: "))
    
    print(f"El resultado de la suma es {numero1 + numero2}")
    
def restar():
    numero1 = int(input("Ingrese el primer valor: "))
    numero2 = int(input("Ingrese el segundo valor: "))
    
    print(f"El resultado de la resta es {numero1 - numero2}")

while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        sumar()        
    elif opcion == 2:
        restar()
    elif opcion == 3:
        break
    else:
        print("Ingrese una opción válida")
        continue
        print("lalalalala")