def obtener_dia(numero):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    
    # Recupera un valor a partir de la llave (numero); el segundo es el valor por defecto (en caso de que la llave no exista en el diccionario)
    return dias.get(numero, "Número no válido")

# Llamada a la función (al "Switch")
print(obtener_dia(4))

# Alternativa con if - elif
numero = 4

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miércoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
else:
    print("Número no válido")