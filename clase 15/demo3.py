class Volador:
    
    def moverse(self):
        print("El pato vuela")
        
class Nadador:
    
    def moverse(self):
        print("El pato nada")
        
class Pato(Volador, Nadador):
    
    pass

pato1 = Pato()
pato1.moverse()

print(Pato.__mro__)
# help(Pato)