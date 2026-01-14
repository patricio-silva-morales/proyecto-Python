computadora = 20
electrodomestico = 50
telefono = 15
accesorios = 25

seleccion = input("Ingrese una categoría: ").lower().strip()

seleccion = seleccion.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

if seleccion == "":
    print("Error: Debe ingresar un valor.")

elif seleccion in ["computadora", "computadoras"]:
    if computadora > 0:
        print("Stock Disponible. "
              "Categoría: Computadoras.")
    else:
        print("Sin Stock.")

elif seleccion in ["electrodomestico", "electrodomesticos"]: 
    if electrodomestico > 0:
        print("Stock Disponible." 
              "Categoría: Electrodomésticos.")
    else:
        print("Sin Stock.")

elif seleccion in ["telefono", "telefonos"]:
    if telefono > 0:
        print("Stock Disponible. Categoría: Teléfonos.")
    else:
        print("Sin Stock.")

elif seleccion == "accesorios":
    if accesorios > 0:
        print("Stock Disponible. Categoría: Accesorios.")
    else:
        print("Sin Stock.") 
else:
    print("Error: El producto no pertenece a ninguna categoría conocida.")