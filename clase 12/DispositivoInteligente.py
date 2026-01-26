class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre          # Atributo público
        self.__salario = salario      # Atributo privado

    def ver_salario(self):
        return self.__salario

    def modificar_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
            print("Salario modificado correctamente.")
        else:
            print("Error: el salario debe ser mayor que 0.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.__salario}")
        print("-" * 30)


# Crear empleados
empleado1 = Empleado("Ana", 1200)
empleado2 = Empleado("Carlos", 1800)

# Mostrar información inicial
empleado1.mostrar_info()
empleado2.mostrar_info()

# Intento incorrecto de modificar salario
empleado1.__salario = -1000  # NO modifica el salario real

print("Después del intento incorrecto:")
empleado1.mostrar_info()

# Modificación correcta usando el método
empleado1.modificar_salario(1500)

print("Después de modificar correctamente:")
empleado1.mostrar_info()