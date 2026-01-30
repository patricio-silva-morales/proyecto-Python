try:

    numero = int(input("Ingresa un número: "))

    resultado = 10 / numero
    
    print("Resultado: ", resultado)
    
except ValueError:
    print("El número no es válido")
    
except ZeroDivisionError:
    print("No es posible dividir por cero")

except Exception:
    print("Algo ocurrió... No sé qué fue.")
    
print("Gracias por usar la aplicación")