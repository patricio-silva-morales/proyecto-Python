# Acumulador suma comienza en 0
suma = 0

for cont in range(1, 6):
    numero = int(input("Ingrese un número: "))
    
    # Sumo el número al valor del acumulador
    suma += numero
    
print("Suma: ", suma)