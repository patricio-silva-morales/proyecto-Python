class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad >= 0:
        print(f"Edad válida: {edad} años")
    else:        
        raise EdadInvalidaError("La edad no puede ser negativa")
        
try:
    validar_edad(25)
    validar_edad(-3)
except EdadInvalidaError as e:
    print(e)