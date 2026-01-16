def dibujar_rectangulo (i,j):
    for i in range(filas):
        for j in range(ancho):
            i = "*"
            j = "*"
            print(j + i, end =" ")
        print()
def dibujar_rectangulo_un_asterisco (i,j):
    for i in range(filas):
        for j in range(ancho):
            j = "⬜"
            print(j, end =" ")
        print()



filas = int(input('ingrese el alto del rectangulo como un número entero: '))
ancho = int(input('ingrese el ancho del rectangulo como un número entero: '))
dibujar_rectangulo(filas,ancho)
dibujar_rectangulo_un_asterisco(filas,ancho)