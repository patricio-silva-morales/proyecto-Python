class Procesador:
    
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad
        
class MemoriaRAM:
    
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo
        
class DiscoDuro:
    
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo
        
class Computadora:
    
    def __init__(self, marca, marca_pro, velocidad_pro, capacidad_ram, tipo_ram, capacidad_dd, tipo_dd):
        self.marca = marca
        
        self.procesador = Procesador(marca_pro, velocidad_pro)
        self.ram = MemoriaRAM(capacidad_ram, tipo_ram)
        self.disco_duro = DiscoDuro(capacidad_dd, tipo_dd)
        
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Procesador: {self.procesador.marca} | {self.procesador.velocidad}")
        print(f"RAM: {self.ram.capacidad} | {self.ram.tipo}")
        print(f"Disco Duro: {self.disco_duro.capacidad} | {self.disco_duro.tipo}")
        
computadora = Computadora("ACER", "Intel", "5.4ghz", "12GB", "DDR5", "2TB", "SSD")
computadora.mostrar_info()

computadora = None

print(computadora)