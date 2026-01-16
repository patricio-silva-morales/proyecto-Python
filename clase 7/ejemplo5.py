inventario = []

nombre = input("Ingrese el nombre del producto: ")
categoria = input("Ingrese la categoría del producto: ")
precio = float(input("Ingrese el precio del producto: "))
stock = int(input("Ingrese el stock del producto: "))

producto = {
    "nombre": nombre,
    "categoria": categoria,
    "precio": precio,
    "stock": stock
}

inventario.append(producto)

if producto["precio"] < 10:
    print("Producto en oferta")