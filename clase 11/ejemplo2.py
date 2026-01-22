class Cliente:
    # Método constructor 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, {self.nombre}")

# Instaciación de clase Cliente         
cliente = Cliente("Pedro", 20) # Llamada al método constructor
cliente.saludar()
cliente.nombre = "Juan"
print(cliente.nombre)