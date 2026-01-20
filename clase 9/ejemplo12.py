# Creamos diccionario
productos = {
    "P001": {
        "nombre": "Teclado",
        "precio": 5000,
        "stock": 10
    },
    "P002": {
        "nombre": "Monitor",
        "precio": 40000,
        "stock": 3
    }
}

" Accedemos al producto mediante su ID"
print(productos["P002"])

productos["P003"] = {
    "nombre": "Mouse",
    "precio": 5000,
    "stock": 15
}

# Modifico stock, accediendo al diccionario interior
productos["P002"]["stock"] = 4
print(productos["P002"])

# Elimino un producto a partir de su ID (clave)
productos.pop("P001")

# Muestra todos los productos
for clave, valor in productos.items():
    print(f"Producto: {valor['nombre']} | Precio: {valor['precio']} | Stock: {valor['stock']}")
    
# Muestra solo los productos con stock < 10
for clave, valor in productos.items():
    if valor['stock'] < 10:
        print(f"Producto: {valor['nombre']} | Precio: {valor['precio']} | Stock: {valor['stock']}")
