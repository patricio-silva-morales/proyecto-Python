class Mascota:
    
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        
    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo} de {self.edad} años.")
        
    def es_joven(self):
        return self.edad < 5

mascotas = []
mascotas.append(Mascota("perrito", 3, "Perro"))
mascotas.append(Mascota("cachorro", 1, "Perro"))
mascotas.append(Mascota("perrito", 8, "Gato"))

for mascota in mascotas:
    mascota.presentarse()
    if mascota.es_joven():
        print("Es joven")