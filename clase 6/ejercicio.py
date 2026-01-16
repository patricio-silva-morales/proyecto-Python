peliculas = {
    1: {"titulo": "Matrix",      "horario": "18:00", "precio": 5000, "disponibles": 20},
    2: {"titulo": "Inception",   "horario": "20:30", "precio": 5500, "disponibles": 15},
    3: {"titulo": "Interstellar","horario": "22:00", "precio": 6000, "disponibles": 10},
}

reservas = []
total_general = 0

while True:
    print("Películas disponibles: ")

    for codigo, datos in peliculas.items():
        print(f"{codigo}. {datos['titulo']} - {datos['horario']} "
              f"(Precio: ${datos['precio']} - Disponibles: {datos['disponibles']})")

    print("0. Finalizar compra")

    opcion = int(input("Seleccione el número de la película (o 0 para finalizar): "))

    if opcion == 0:
        break

    if opcion not in peliculas:
        print("Opción inválida. Intente nuevamente.")
        continue

    pelicula = peliculas[opcion]

    cantidad = int(input(f"Ingrese la cantidad de boletos para '{pelicula['titulo']}': "))

    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
        continue

    if cantidad > pelicula["disponibles"]:
        print("No hay suficientes boletos disponibles.")
        print(f"Boletos disponibles: {pelicula['disponibles']}")
        continue

    subtotal = cantidad * pelicula["precio"]
    pelicula["disponibles"] -= cantidad
    total_general += subtotal

    reservas.append({
        "titulo": pelicula["titulo"],
        "horario": pelicula["horario"],
        "cantidad": cantidad,
        "subtotal": subtotal
    })

    print(f"Reserva realizada: {cantidad} boleto(s) para '{pelicula['titulo']}'")
    print(f"Subtotal: ${subtotal}")

    seguir = input("¿Desea hacer otra reserva? (s/n): ").lower()
    if seguir != "s":
        break

if len(reservas) == 0:
    print("No se realizaron reservas.")
else:
    for i, reserva in enumerate(reservas, start=1):
        print(f"Reserva {i}:")
        print(f"Película : {reserva['titulo']}")
        print(f"Horario  : {reserva['horario']}")
        print(f"Boletos  : {reserva['cantidad']}")
        print(f"Subtotal : ${reserva['subtotal']}")

    print(f"Total a pagar: ${total_general}")    