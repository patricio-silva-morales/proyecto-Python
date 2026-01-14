def consulta(opcion):
    dict = {
        1: "Consultar saldo",
        2: "Transferencias",
        3: "Pago de servicios",
        4: "Préstamos y créditos",
        5: "Atención al cliente"
    }
    
    return dict.get(opcion, "Opción inválida. Intente con un número del 1 al 5")

opcion_seleccionada = int(input("Ingrese una opción entre 1 y 5: "))

print(f"La respuesta es {consulta(opcion_seleccionada)}")