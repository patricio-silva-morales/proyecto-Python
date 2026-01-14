pelicula = input("Ingrese el nombre de la película: ")
disponible = input("¿Está disponible? (sí/no): ")

if disponible.lower() == "sí":
    genero = input("Ingrese el género (acción, drama, comedia, terror): ")
    
    if genero.lower() == "acción":
        print("La película es de acción. ¡Ideal para disfrutar mucha adrenalina!")
    elif genero.lower() == "drama":
        print("La película es un drama. Prepárate para una historia intensa.")
    elif genero.lower() == "comedia":
        print("La película es una comedia. ¡Risas aseguradas!")
    elif genero.lower() == "terror":
        print("La película es de terror. ¡No apta para corazones sensibles!")
    else:
        print("No tengo información sobre ese tipo de género.")
else:
    print("La película no se encuentra en el catálogo por ahora.")