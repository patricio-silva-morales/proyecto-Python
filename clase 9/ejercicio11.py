# Diccionario original
usuario = {
    "nombre": "Luis",
    "edad": 25
}

# Si la clave no existe, se agrega; si ya existe, NO se modifica
usuario.setdefault("pais", "Chile")
usuario.setdefault("edad", 20)

print(usuario)

# Se envía un diccionario para fusionar con USUARIO
# Si la clave existe, se modifica el valor; si no existe, se agrega
usuario.update({
    "edad": 31,
    "email": "algo@algo.cl"
})

print(usuario)