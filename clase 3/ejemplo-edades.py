edad = int(input("Ingrese una edad: "))

if edad < 0:
    print("La edad no es válida")
elif edad <= 12:
    print("Es niña(o)")
elif edad <= 17:
    print("Es adolescente")
elif edad <= 64:
    print("Es adulto")
else:
    print("Es adulto mayor")