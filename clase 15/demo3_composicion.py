class Volador:
    def moverse(self):
        print("El pato vuela")


class Nadador:
    def moverse(self):
        print("El pato nada")


class Pato:
    def __init__(self):
        self.volador = Volador()
        self.nadador = Nadador()

    def volar(self):
        self.volador.moverse()

    def nadar(self):
        self.nadador.moverse()
        
pato1 = Pato()
pato1.volar()
pato1.nadar()