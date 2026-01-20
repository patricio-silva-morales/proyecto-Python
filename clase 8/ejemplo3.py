# Creación de tupla
coordenadas = (-34.983, -71.239)

# Muestra tupla
#print(coordenadas)

# Recupera elementos de tupla por posición (índice)
#print(f"Latitud: {coordenadas[0]}")
#print(f"Longitud: {coordenadas[1]}")

# Esta línea provoca un error, dado que las tuplas son inmutables
# coordenadas[0] = 10.765

# Reemplazar tupla por una nueva
coordenadas = (-39.814167, -73.245833)

# Muestra tupla
#print(coordenadas)

# Lista de coordenadas de cada ciudad
ciudades = [(-34.983, -71.239), (-39.814167, -73.245833), (-36.77, -73.05)]

# Muestra las coordanadas de cada ciudad 
# (Ciudades es la lista y Ciudad es una tupla)
for ciudad in ciudades:
    print(f"La ciudad está ubicada en ({ciudad[0]}, {ciudad[1]})")
    
# Muestra la longitud de Concepción
print(f"La longitud de Valdivia es {ciudades[2][1]}")