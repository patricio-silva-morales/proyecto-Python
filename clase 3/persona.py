class Persona:
    
    # Método constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre    # Atributo nombre
        self.edad = edad        # Atributo edad

# Creación de instancia de la clase (Instanciación)        
persona1 = Persona("Juan", 25) # Objeto persona1
persona2 = Persona("Ana", 21) # Objeto persona2

# print(f"La persona se llama {persona1.nombre} y tiene {persona1.edad} años de edad")
print(f"La persona se llama {persona2.nombre} y tiene {persona2.edad} años de edad")

persona2.edad = 23

print(f"La persona se llama {persona2.nombre} y tiene {persona2.edad} años de edad")
