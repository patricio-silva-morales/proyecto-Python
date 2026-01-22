class Celular:
    def __init__(self, marca, modelo, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento

    def encender(self):
        print(
            f"Encendiendo celular {self.marca} {self.modelo} "
            f"con {self.almacenamiento} GB de almacenamiento"
        )

    def mostrar_info(self):
        print("Información del celular:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print("--------------------")


celular1 = Celular("Apple", "iPhone 14 Pro", 256)
celular2 = Celular("Samsung", "A55", 128)

celular1.encender()
celular1.mostrar_info()

celular2.encender()
celular2.mostrar_info()