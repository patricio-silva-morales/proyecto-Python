def velocidad(viento):
    if viento < 1:
        return "Calma"
    elif viento <= 20:
        return "Brisa Ligera"
    elif viento <= 40:
        return "Viento Moderado"
    elif viento <= 70:
        return "Viento Fuerte"
    else:
        return "Extremo"   
     
print ("----Programa velocidad de vientos----")
while True:
    try:  
        velocidad_viento = float(input("Ingrese la velocidad del viento en km/h:.. "))
        print(f"La velocidad del viento se clasifica como: {velocidad(velocidad_viento)}")
        continuar = input("Quiere consultar otra velocidad de viento? (Si / No):...")
        if continuar == "No":
            break
    
    except ValueError: 
        print("---Debe ingresar una velocidad correcta, en numeros---")
        continue

print ("---Gracias por utilizar nuestro programa---")