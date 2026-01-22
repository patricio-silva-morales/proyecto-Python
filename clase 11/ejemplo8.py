class Automovil:
    
    def __init__(self):
        self.encendido = False
        self.combustible = 0
        self.velocidad = 0
        
    def encender(self):
        if self.combustible > 0 and not(self.encendido):
            self.encendido = True
            print("Encendido")
    
    def acelerar(self):
        if self.encendido:
            self.velocidad += 1
            self.combustible -= 0.01
            print("Aceleró")
            
automovil1 = Automovil()

automovil1.combustible = 20

automovil1.encender()

print(automovil1.velocidad)
print(automovil1.combustible)

for i in range(50):
    automovil1.acelerar()
        
print(automovil1.velocidad)
print(automovil1.combustible)
    