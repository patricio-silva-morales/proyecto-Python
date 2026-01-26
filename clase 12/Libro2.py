class Libro:

    def __init__(self, titulo, autor, anio, precio, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.__precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, monto):
        if monto > 0:
            self.__precio = monto
        else:
            print("El precio no es válido")
            self.__precio = None

    def vender(self, unidades):
        if unidades <= 0:
            print("No se pueden vender cero productos.")
            return

        if self.cantidad >= unidades:
            self.cantidad -= unidades
            total = unidades * self.__precio
            print(f"Se vendieron {unidades} unidades de '{self.titulo}'. Total: {total} pesos.")
        else:
            print(f"No hay stock suficiente de '{self.titulo}'. Solo quedan {self.cantidad} unidades.")


libro1 = Libro("El camino de las bestias", "Carlos Pinto", 2025, 12500, 10)
libro2 = Libro("Hail Mary", "Andrew Weir", 2022, 15000, 5)

libro1.mostrar_info()
print("---")
libro2.mostrar_info()
print("---")
libro1.set_precio(20000)
libro1.mostrar_info()
print("---")
libro2.set_precio(-1000)
libro2.mostrar_info()
print("---")
libro1.vender(3)    
libro1.mostrar_info()
print("---")
libro2.vender(10)  
libro2.mostrar_info()