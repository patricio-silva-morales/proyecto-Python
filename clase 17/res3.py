def km_a_millas():
    while True:
        try:
            km = float(input("Ingrese la distancia en KM (se puede ingresar con decimal):.. "))
            resultado = (km/1.60934)
          
        except ValueError:
            print("Entrada invalida. Debes ingresar numeros enteros")
            continue

        #Extra Si se cierra el proceso con control + c 
        except KeyboardInterrupt:
            print("Proceso cancelado por el usuario.")
            break

        else:
            print(f"El resultado es: {round(resultado,2)}")
            break

        finally:
            print("-- Proceso finalizado --")


km_a_millas()