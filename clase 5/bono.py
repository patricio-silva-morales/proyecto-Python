#solucion Ia
def obtener_bono(rango):
    tabla = {1: 12000, 2: 20000, 3: 35000, 4: 52000, 5: 78000}
    return tabla.get(rango) # Retorna None si no existe

# Lógica de interacción
try:
    opcion = int(input("Ingrese una opción (1-5): "))
    resultado = obtener_bono(opcion)

    if resultado:
        print(f"El bono es: ${resultado:,}")
    else:
        print("Opción inválida.")
except ValueError:
    print("Debe ingresar un número entero.")