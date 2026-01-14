contador = 0
salir = 0

while contador < 5 and salir == 0:
    print(f"Número {contador}")
    
    contador += 1
    
    salir = int(input("¿Desea salir? (Sí=1/No=0): "))
