class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def emitir_sonido(self):
        print("Sonido genérico")
        
class Perro(Animal):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def emitir_sonido(self):
        print("Guau!!!")
        
class Gato(Animal):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def emitir_sonido(self):
        print("Miau!!!")
        
perro1 = Perro("Bruce")
gato1 = Gato("Don René")

perro1.emitir_sonido()
gato1.emitir_sonido()