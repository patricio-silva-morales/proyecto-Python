class Libro:
    
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año
        
    def mostrar_info(self):
        print(f"Título: {self.__titulo} | Autor: {self.__autor} | Año: {self.__año}")
        
libro1 = Libro("El camino de las bestias", "Carlos Pinto", 2025)
libro2 = Libro("Hail Mary", "Andy Weir", 2022)

libro1.mostrar_info()
libro2.mostrar_info()
