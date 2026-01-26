class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular       # PÚBLICO: Cualquiera sabe el dueño
        self._tipo_cuenta = "Ahorro" # PROTEGIDO: Uso interno/herencia
        self.__saldo = saldo         # PRIVADO: ¡Nadie toca la plata directo!

    def ver_saldo_oficial(self):
        # La clase SÍ puede ver sus propios privados
        return self.__saldo

cuenta = CuentaBancaria("Pedro", 1000)

# 1. Acceso Público: OK
print(cuenta.titular)      # Imprime: Pedro

# 2. Acceso Protegido: FUNCIONA (pero no deberías hacerlo)
print(cuenta._tipo_cuenta) # Imprime: Ahorro (Python te deja, pero es mala práctica)

# 3. Acceso Privado: ERROR
print(cuenta.__saldo)    # AttributeError: 'CuentaBancaria' object has no attribute '__saldo'