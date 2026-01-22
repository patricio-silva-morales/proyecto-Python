class Persona:
    
    def __init__(self, parametro_nombre, parametro_edad):
        self.nombre = parametro_nombre
        self.edad = parametro_edad
        
    def presentarse(self):
        print(f"Buenos días, mi nombre es {self.nombre} y tengo {self.edad} años de edad")
        
    def cumplir_anios(self):
        self.edad += 1
        
persona1 = Persona("Ana", 30)
persona2 = Persona("Mario", 25)

persona1.presentarse()
persona2.presentarse()

print(persona1.edad)
print(persona2.edad)

persona1.cumplir_anios()
persona2.cumplir_anios()

print(persona1.edad)
print(persona2.edad)