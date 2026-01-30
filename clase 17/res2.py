def division_segura():

    while True:
        try:
            n1 = input("Ingresa el primer número: ")
            num1 = float(n1)

            n2 = input("Ingresa el segundo número: ")
            num2 = float(n2)

            resultado = num1 / num2

        except ValueError:
            print("Ingrese solo números")

        except ZeroDivisionError:
            print("No se puede dividir por cero")

        else:
            print(f"Resultado: {resultado}")
            break

        finally:
            print("Intento finalizado")

print("Iniciando programa de división")
division_segura()