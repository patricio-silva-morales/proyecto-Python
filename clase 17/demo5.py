try:
    numero = int(input("Ingrese un número entero: "))

except ValueError:
    print("El número no es válido.")
    
except Exception:
    print("Ha ocurrido un error.")