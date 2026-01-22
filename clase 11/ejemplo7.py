class Auto:
    
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.velocidad = 0
        
    def acelerar(self):
        if self.velocidad < 230:
            self.velocidad += 1
            
    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 1
            
    def ver_estado(self):
        print(self.marca)
        print(self.color)
        print(self.velocidad)
            
auto1 = Auto("Mazda", "azul")
auto2 = Auto("Chevrolet", "blanco")

auto1.ver_estado()
auto2.ver_estado()

for i in range(500):
    auto1.acelerar()
    
for i in range(40):
    auto2.frenar()
    
auto1.ver_estado()
auto2.ver_estado()
    