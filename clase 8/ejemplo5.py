# Creamos listas con duplicados
lista1 = ["Ana", "Luis", "Pedro", "Ana", "Marcelo", "Pedro"]
lista2 = ["Sandra", "David", "Luis", "Pedro", "Sandra", "Carlos", "David"]

# Creamos sets a partir de las listas
set1 = set(lista1)
set2 = set(lista2)

# Contrastamos listas y sets
print(f"Lista: {lista1}")
print(f"Set: {set1}")
print(f"Lista: {lista2}")
print(f"Set: {set2}")

# Intersección entre ambos conjuntos
interseccion = set1 & set2
print(f"Intersección: {interseccion}")

# Unión de ambos conjuntos
union = set1 | set2
print(f"Unión: {union}")

# Diferencia entre set1 y set2
diferencia1 = set1 - set2
print(f"Diferencia 1: {diferencia1}")

# Diferencia entre set2 y set1
diferencia2 = set2 - set1
print(f"Diferencia 2: {diferencia2}")

# Agrego elementos al conjunto
set1.add("Javier")
set1.add("Javier")

# Remuevo un elemento del conjunto
set1.remove("Ana")

# Muestro el contenido del set1
print(f"Set 1: {set1}")

# Recorro el set1 y muestro cada usuario 
for usuario in set1:
    print(usuario)