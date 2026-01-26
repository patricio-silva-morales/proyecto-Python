class Empleado:
    # Atributo de clase
    aumento_general = 1.05
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
    @classmethod
    def cambiar_aumento(cls, nuevo_aumento):
        cls.aumento_general = nuevo_aumento
        
    @staticmethod
    def salario_umbral(salario, umbral = 539000):
        return salario > umbral
    
t1 = Empleado("Ana", 600000)
t2 = Empleado("Juan", 450000)
t3 = Empleado("María", 500000)

print(t1.salario * Empleado.aumento_general) # Obtenemos el valor del atributo de clase
print(t2.salario * Empleado.aumento_general)
print(t3.salario * Empleado.aumento_general)

# Llamamos al método de clase que modifica el valor el atributo de clase
Empleado.cambiar_aumento(1.1)

print(t1.salario * Empleado.aumento_general)
print(t2.salario * Empleado.aumento_general)
print(t3.salario * Empleado.aumento_general)

print(Empleado.salario_umbral(t1.salario))
print(Empleado.salario_umbral(t2.salario))
print(Empleado.salario_umbral(t3.salario))