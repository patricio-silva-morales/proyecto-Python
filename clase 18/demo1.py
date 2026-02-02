def validar_edad(edad):
    if edad >= 0:
        print(f"Edad válida: {edad} años")
    else:        
        raise ValueError("La edad no puede ser negativa")
        
try:
    validar_edad(25)
    validar_edad(-3)
except ValueError as e:
    print(e)