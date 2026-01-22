class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print("Habló...")
        
mi_gato = Animal("Luna")
mi_gato.hablar()

mi_perro = Animal("Negrita")

if isinstance(mi_gato, Animal):
    print("El objeto es instancia de la clase Animal")
    
mis_mascotas = []
mis_mascotas.append(mi_gato)
mis_mascotas.append(mi_perro)

for mascota in mis_mascotas:
    print(mascota.nombre)