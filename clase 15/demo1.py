class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f"Buenos días. Soy {self.nombre} y tengo {self.edad} años de edad"

class Empleado(Persona):
    
    def __init__(self, cargo, nombre, edad):
        super().__init__(nombre, edad) # Llamada al constructor del padre (superclase)
        self.cargo = cargo # Atributo propio de Empleado
        
    def presentarse(self):
        return f"Buenos días. Soy {self.nombre} y tengo {self.edad} años de edad. Me desempeño como {self.cargo}"
    
    def trabajar(self):
        return f"Me desempeño como {self.cargo}"
    
empleado1 = Empleado("Desarrollador Back-End", "Rigoberto", 65)
print(empleado1.presentarse())
print(empleado1.trabajar())