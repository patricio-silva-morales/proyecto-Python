# Estructura de datos (diccionario) con un elemento
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Arica",
    "matriculado": False
}

# Muestra el contenido del diccionario
print(persona)

# Muestra el tipo de variable
print(type(persona))

# Cambio uno de los valores; la estructura es MUTABLE
persona["edad"] = 32
print(persona)

print(type(persona["nombre"]))
print(type(persona["edad"]))
print(type(persona["ciudad"]))
print(type(persona["matriculado"]))