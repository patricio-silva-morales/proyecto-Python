class Persona:
    
    def __init__(self, nombre = ""):
        self.nombre = nombre
        
    def __str__(self):
        return f"La persona se llama {self.nombre}"
        
    def saludar(self, *args):
        if len(args) == 0:
            print("Hola!")
        elif len(args) == 1:
            print(f"Hola {args[0]}")
        elif len(args) == 2:
            print(f"Hola {args[0]} de {args[1]}")
        
persona1 = Persona("David")
persona1.saludar()
persona1.saludar("Iris")
persona1.saludar("Gustavo", "Illapel")

print(persona1)