# Gestión de retiros bancarios

retiros = []

print("CARGA DE RETIROS")
while True:
    try:
        entrada = input("Monto (fin para terminar): ").lower()
        
        if entrada == "fin":
            break
        
        monto = float(entrada)
        
        if monto <= 0:
            print("Monto inválido")
        else:
            retiros.append(monto)
            print("Agregado")
    
    except ValueError:
        print("Dato no numérico")

if not retiros:
    print("Sin retiros")
else:
    print("Lista:", retiros)

    print("\nCALCULO")
    while True:
        try:
            divisor = float(input("Divisor: "))
            
            if divisor == 0:
                print("No puede ser cero")
            else:
                print("Resultado:", sum(retiros) / divisor)
                break
        except ValueError:
            print("Dato no numérico")

    print("\nCONSULTA")
    while True:
        try:
            pos = int(input("Posición: "))
            
            print("Monto:", retiros[pos])
            break
        
        except ValueError:
            print("Debe ser entero")
        
        except IndexError:
            print("Posición inválida")

print("Fin del programa")