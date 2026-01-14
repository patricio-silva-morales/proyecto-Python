print("1. Entrada cliente regular")
print("2. Entrada estudiante")
print("3. Entrada jubilado")
tipo_entrada = int(input("Ingrese tipo de entrada (1-3): "))

if tipo_entrada == 1:
    print(f"El valor de la entrada es 5000")
elif tipo_entrada == 2:
    print(f"El valor de la entrada es 2500")
elif tipo_entrada == 3:
    print(f"El valor de la entrada es 3000")
else:
    print("Tipo no válido")