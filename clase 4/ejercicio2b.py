# Películas iniciales
pelicula1 = "matrix"
genero1 = "acción"

pelicula2 = "titanic"
genero2 = "drama"

pelicula3 = "mi pobre angelito"
genero3 = "comedia"

nombre = input("Ingrese el nombre de la película: ").lower()

if nombre == pelicula1:
    genero = genero1
elif nombre == pelicula2:
    genero = genero2
elif nombre == pelicula3:
    genero = genero3
else:
    genero = ""

if genero == "":
    print("La película no se encuentra en el catálogo por ahora.")
else:
    if genero == "acción":
        print("La película es de acción. ¡Ideal para disfrutar mucha adrenalina!")
    elif genero == "drama":
        print("La película es un drama. Prepárate para una historia intensa.")
    elif genero == "comedia":
        print("La película es una comedia. ¡Risas aseguradas!")
    elif genero == "terror":
        print("La película es de terror. ¡No apta para corazones sensibles!")
    else:
        print("No tengo información sobre ese tipo de género.")
