#Sistema de Reservas en un hotel

#Definición de las habitaciones y sus precios
habitaciones = {
    1: ("Económica", 35000),
    2: ("Estándar", 50000),
    3: ("Superior", 65000),
    4: ("Suite", 90000),
    5: ("Presidencial", 150000)
}

#Solicitud de entrada al usuario
tipo_habitacion = int(input("Ingrese tipo de habitación (1 a 5): "))

#Validación switch
info_habitacion = habitaciones.get(tipo_habitacion)

#Verificación de validez
if info_habitacion is None:
    print("Tipo de habitación inválido. Debe ingresar un número entre 1 y 5.")
else:
    categoria = info_habitacion[0]
    precio_por_noche = info_habitacion[1]

    #Solicitud de entrada al usuario
    noches = int(input("Ingrese cantidad de noches: "))

    if noches <= 0:
        print("El mínimo de estadía es de 1 noche. Vuelva a ingresar la cantidad de noches a reservar.")
    
    #Resultado en pantalla
    else:
        total_pagar = precio_por_noche * noches

        print("\n--- RESUMEN DE SU RESERVA ---")
        print("Categoría de habitación:", categoria)
        print("Precio por noche: $", precio_por_noche)
        print("Total de noches:", noches)
        print("Total a pagar: $", total_pagar)