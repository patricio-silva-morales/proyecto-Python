pin_correcto = "1234"

intentos = 3

while intentos > 0:
    print(f"Cuenta con {intentos} intento(s).")
    pin = input("Ingrese un pin: ")
    
    if pin == pin_correcto:
        print("Bienvenido!!!")
        break
    
    intentos -= 1
    
if intentos == 0:
    print("Acceso bloqueado")