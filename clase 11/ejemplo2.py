class Cliente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, {self.nombre}")
        
cliente = Cliente("Pedro", 20)
cliente.saludar()