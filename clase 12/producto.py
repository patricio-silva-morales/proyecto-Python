class Producto:
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.set_precio(precio)
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, monto):
        if monto > 0:
            self.__precio = monto
        else:
            print("El precio no es válido")
            self.__precio = None        
            
producto1 = Producto("Jabón", -1000)
print(producto1.get_precio())
producto1.set_precio(-1000)
producto1.set_precio(2000)
print(producto1.get_precio())