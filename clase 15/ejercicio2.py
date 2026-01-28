class Volador:
    def moverse(self):
        print("Estoy volando")

class Nadador:
    def moverse(self):
        print("Estoy nadando")

class Pato(Volador, Nadador):
    pass

print ("---pato - moverse---")
pato = Pato()

print ("2 orden de resolucion A")
pato.moverse()
print(Pato.__mro__)

class Pato(Nadador, Volador):
    pass

pato = Pato()
print ("2 orden de resolucion B")

pato.moverse()
print(Pato.__mro__)


print ("Moverse completo")
class Pato(Volador, Nadador):
    def moverse_completo(self):
        Volador.moverse(self)
        Nadador.moverse(self)

pato = Pato()
pato.moverse_completo()