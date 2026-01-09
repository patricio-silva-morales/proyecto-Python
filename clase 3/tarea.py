# 1. Definir la clase 
class Coche:
    def __init__(self, marca, modelo, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje

# 2. Pedir los datos 
print("Registro de Vehículo")
marca_input = input("Ingrese la marca: ")
modelo_input = input("Ingrese el modelo: ")
km_input = int(input("Ingrese el kilometraje: "))

mi_coche = Coche(marca_input, modelo_input, km_input)

# 3. Evaluar nuevo/usado
if mi_coche.kilometraje == 0:
    estado = "Nuevo"
else:
    estado = "Usado"

print(f"Estado Vehiculo: {estado}")

# 4. Menú 
while True:
    print("\n Menú de Modificación")
    print("1. Modificar Marca")
    print("2. Modificar Modelo")
    print("3. Modificar Kilometraje")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    # 5. Implementar break 
    if opcion == "4":
        print("Saliendo del menú")
        break
    
    # 6.Validacion
    if opcion not in ["1", "2", "3", "4"]: #lista con las opciones que di antes
        print("Opción no válida. Intente de nuevo.")
        continue

    # modificar con opcion correcta
    if opcion == "1":
        mi_coche.marca = input("Nueva marca: ")
    elif opcion == "2":
        mi_coche.modelo = input("Nuevo modelo: ")
    elif opcion == "3":
        mi_coche.kilometraje = int(input("Nuevo kilometraje: ")) # el int es para que sea un numero

# 7. Mostrar información final
print("\n   Información Final del Vehículo   ")
print(f"Marca: {mi_coche.marca}")
print(f"Modelo: {mi_coche.modelo}")
print(f"Kilometraje: {mi_coche.kilometraje} km")
print(f"Estado: {'Nuevo' if mi_coche.kilometraje == 0 else 'Usado'}")