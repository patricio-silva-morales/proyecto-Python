class Figura:
    
    # Método no implementado (abstracto)
    def dibujar(self):
        pass
    
class Rectangulo(Figura):
    
    def dibujar(self):
        return "Dibujo un rectángulo"
    
class Circulo(Figura):
    
    def dibujar(self):
        return "Dibujo un círculo"
    
class Triangulo(Figura):
    
    def dibujar(self):
        return "Dibujo un triángulo"
    
figuras = []
figuras.append(Rectangulo())
figuras.append(Triangulo())
figuras.append(Rectangulo())
figuras.append(Circulo())
figuras.append(Circulo())
figuras.append(Figura())

for figura in figuras:
    print(figura.dibujar())