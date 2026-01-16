meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

dia = int(input("Ingrese un número entre 1 y 12: "))

if meses.get(dia) != None:
    print(f"El número corresponde a {meses[dia]}")
else:
    print("Ingrese un valor válido")