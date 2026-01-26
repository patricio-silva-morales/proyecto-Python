class Producto:
    # Atributo de clase
    descuento = 0.05 # 5%

    def __init__(self, nombre, precio):
        # Hacemos uso del método estático en la instanciación de la clase
        if Producto.validar_precio(precio):
            self.nombre = nombre # Atributo público
            self.__precio = precio # Atributo privado
        else:
            self.__precio = 0

    def aplicar_descuento(self):
        # Accedemos al atributo de clase: Producto.descuento
        return self.__precio * (1 - Producto.descuento)

    @classmethod
    def set_descuento(cls, nuevo_descuento):
        # Modificamos el atributo de clase
        cls.descuento = nuevo_descuento

    @staticmethod
    def validar_precio(precio):
        return precio > 0

p1 = Producto("Plato", 4000)
p2 = Producto("Tazón", 2600)

print(p1.aplicar_descuento())
print(p2.aplicar_descuento())

Producto.set_descuento(0.1) # 1%

print(p1.aplicar_descuento())
print(p2.aplicar_descuento())