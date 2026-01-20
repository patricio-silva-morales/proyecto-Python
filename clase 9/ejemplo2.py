# Definimos un usuario mediante un diccionario
usuario = {
    "nombre": "Marcela",
    "edad": 25,
    "email": "marcela@gmail.com"
}

# Muestro directamente los valores
print(usuario["nombre"])
print(usuario["edad"])
print(usuario["email"])

# Modifico la edad
usuario["edad"] = 27

# Muestro directamente los valores
print(usuario["nombre"])
print(usuario["edad"])
print(usuario["email"])

# Agrego un nuevo elemento (clave|valor)
usuario["pais"] = "Chile"

# Muestro directamente los valores
print(usuario["nombre"])
print(usuario["edad"])
print(usuario["email"])
print(usuario["pais"])

# Elimino un elemento del diccionario a través de la clave
usuario.pop("email")
# Esta línea marcará error, pues ahora la clave NO existe
# print(usuario["email"])

# Muestra las claves del diccionario
print(usuario.keys())
# Muestra los valores del diccionario
print(usuario.values())
# Muestra los elementos (clave|valor) del diccionario
print(usuario.items())

# Recorro el diccionario, mostrando los elementos (clave|valor)
for clave, valor in usuario.items():
    print(f"{clave} | {valor}")

# Accedo a claves (una existe, la otra no), sin mensajes de error
print(usuario.get("nombre"))
print(usuario.get("teléfono", "La clave indicada no existe"))