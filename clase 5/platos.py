def buscar_platillo(dia):
    platillos = {
        1: "Pollo con arroz",
        2: "Porotos granados",
        3: "Arrollado",
        4: "Tallarines con salsa bolognesa",
        5: "Pescado frito",
        6: "Pizza",
        7: "Ensaladas"
    }
    return platillos.get(dia, "Ingrese un día válido (1 - 7)")

dia = int(input("Indique el día de la semana (1 - 7): "))

print(buscar_platillo(dia))