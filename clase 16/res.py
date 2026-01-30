class Producto:
    def __init__(self,nombre,precio):
        self._nombre = nombre
        self._precio = precio

    def calcular_precio (self):
        return self._precio

    def get_nombre(self):
        return self._nombre

class ProductoFisico(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
    

class ProductoDigital(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

class Suscripcion(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)


productos = []
productos.append(ProductoDigital('a',50000))
productos.append(Suscripcion('b',15000))
productos.append(ProductoFisico('c',10000))
productos.append(ProductoDigital('d',5000))
productos.append(ProductoFisico('e',25000))
productos.append(ProductoDigital('f',10000))
productos.append(Suscripcion('g',7000))

dicc_productos = {
    'Fisico':[],
    'Digital':[],
    'Suscripcion':[]
}
descuento_dig = 0.9
tasa_suscripcion = 1.1

for producto in productos:
    if isinstance(producto,ProductoDigital):
        precio = producto.calcular_precio()
        precio_final = precio * descuento_dig
        lista_diccionario = dicc_productos['Digital']
        agregar_producto = [producto.get_nombre(),precio_final]
        lista_diccionario.append(agregar_producto)
    
    elif isinstance(producto,Suscripcion):
        precio = producto.calcular_precio()
        precio_final = precio * tasa_suscripcion
        lista_diccionario = dicc_productos['Suscripcion']
        agregar_producto = [producto.get_nombre(),precio_final]
        lista_diccionario.append(agregar_producto)

    elif isinstance(producto,ProductoFisico):
        precio = producto.calcular_precio()
        costo_envio = 5000
        precio_final = precio + costo_envio
        lista_diccionario = dicc_productos['Fisico']
        agregar_producto = [producto.get_nombre(),precio_final]
        lista_diccionario.append(agregar_producto)

print('Los productos digitales son: ')
print(dicc_productos['Digital'])        
print('Los productos Fisicos son: ')
print(dicc_productos['Fisico'])
print('Los productos por suscripcion son: ')
print(dicc_productos['Suscripcion'])