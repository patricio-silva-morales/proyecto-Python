from operaciones import sumar # Importación de la función sumar()

numero1 = int(input("Ingrese el primer número: ")) # El valor se convierte a entero
numero2 = int(input("Ingrese el segundo número: ")) # El valor se convierte a entero

# Salida formateada
print(f"El resultado de la suma entre los números es {sumar(numero1, numero2)}")