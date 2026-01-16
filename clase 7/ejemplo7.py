def clasificacion(grados):
    if grados < 5:
        return "Muy frío"
    elif grados < 15:
        return "Frío"
    elif grados < 25:
        return "Agradable"
    elif grados < 35:
        return "Caluroso"
    else:
        return "Extremo"    

try:
    temperatura = int(input("Ingrese la temperatura en grados Celsius: "))

    print(f"Su temperatura se clasifica como: {clasificacion(temperatura)}")
    
except ValueError:
    print("Debe ingresar un número entero")