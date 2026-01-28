class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    def moverse(self):
        print(f'El {self._marca} modelo {self._modelo} se mueve por la carretera')

class Auto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def moverse(self):
        print(f'El {self._marca} modelo {self._modelo} se conduce por la carretera')

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
    def moverse(self):
        print(f'La {self._marca} modelo {self._modelo} se está pedaleando en la carretera')

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self._cilindrada = cilindrada

auto1 = Auto('Mazda','Mx5')
auto2 = Auto('Subaru','Impreza')
auto3 = Auto('Ford','Focus')
auto4 = Auto('Uaz','Hunter')

bicicleta1 = Bicicleta('Treck','520')
bicicleta2 = Bicicleta('Koga','Miyata')
bicicleta3 = Bicicleta('Surly','Ogre')

moto1 = Motocicleta('Honda','Navi',109)
moto2 = Motocicleta('Yamaha','YBR',125)

lista_vehiculos = [auto1, auto2, auto3, auto4, bicicleta1, bicicleta2, bicicleta3, moto1, moto2]

for elemento in lista_vehiculos:
    elemento.moverse()
    if isinstance(elemento, Motocicleta):
        print(f'Cuenta con una cilindrada de {elemento._cilindrada}')