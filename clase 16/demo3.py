class MedioPago:
    
    # Método no implementado (abstracto); clases hija la implementarán
    def pagar(self, monto):
        pass
        
class TarjetaCredito(MedioPago):
    
    def __init__(self, interes):
        # Interés porcentual: Característica propia de la clase TarjetaCredito (atributo)
        self.interes = interes
    
    def pagar(self, monto):
        # Lógica: Devuelve monto a pagar, aplicando interés porcentual (atributo)
        
        # return monto * (1 + self.interes / 100)
        return monto + (monto * self.interes / 100)
    
class Efectivo(MedioPago):
    
    def pagar(self, monto):
        # Lógica: Devuelve el monto a pagar, sin aplicar interés o descuento
        
        return monto
    
class Transferencia(MedioPago):
    
    def __init__(self, descuento):
        # Descuento porcentual: Característica propia de la clase Transferencia (atributo)
        self.descuento = descuento
        
    def pagar(self, monto):
        # Lógica: Devuelve el monto a pagar, restando el descuento porcentual aplicado
        
        # return monto * (1 - self.descuento / 100)
        return monto - (monto * self.descuento / 100)
    
formas_de_pago = []

formas_de_pago.append(TarjetaCredito(5)) # Interés del 5%
formas_de_pago.append(Efectivo())
formas_de_pago.append(Transferencia(10)) # Descuento del 10%

for pago in formas_de_pago:
    print(pago.pagar(80000))