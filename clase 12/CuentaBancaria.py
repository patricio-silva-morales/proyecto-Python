class CuentaBancaria:
    
    # Método constructor
    def __init__(self, saldo, titular):
        self.__saldo = saldo # Atributo privado
        self.titular = titular # Atributo público
        
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            
    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
            
    def ver_saldo(self):
        return self.__saldo
    
cuenta1 = CuentaBancaria(10000, "Vania")
print(cuenta1.ver_saldo())
print(cuenta1.titular)