# Listas iniciales con colores 
catalogo_a = ["rojo", "azul", "verde", "amarillo", "negro", "blanco", "rojo", "azul"]
catalogo_b = ["verde", "morado", "naranja", "negro", "rosa", "blanco", "verde"]

# Convertir listas a sets 
set_a = set(catalogo_a)
set_b = set(catalogo_b)

# Mostrar resultados basicos
print("Todos los colores disponibles:", set_a.union(set_b))
print("Colores en ambos catalogos:", set_a.intersection(set_b))
print("Colores exclusivos de A:", set_a - set_b)
print("Colores exclusivos de B:", set_b - set_a)

# Agregar un nuevo color
nuevo_color = input("\nIngrese un nuevo color para agregar al catalogo A: ")
set_a.add(nuevo_color)
print("Set A actualizado:", set_a)

# Eliminar un color
color_eliminar = input("Ingrese un color para eliminar del catalogo B: ")
set_b.discard(color_eliminar)
print("Set B actualizado:", set_b)

# Mostrar resultados finales
print("\nResultados finales:")
print("Union de A y B:", set_a.union(set_b))
print("Interseccion de A y B:", set_a.intersection(set_b))
print("Colores exclusivos de A:", set_a - set_b)
print("Colores exclusivos de B:", set_b - set_a)