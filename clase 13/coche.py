class Motor:
    
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
        
    def encender(self):
        print("Motor encendido")
        
class Coche:
    
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        
    def arrancar(self):
        self.motor.encender()
        
motor1 = Motor("Bencinero", "2000")
coche1 = Coche("Mazda", "cx-9", motor1)

coche1.arrancar()