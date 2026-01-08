import operaciones

from calculadora import Calculadora

# Llamadas a la funciones
print(operaciones.sumar(4,5))
print(operaciones.restar(4,5))

# Crear (instanciar) el objeto a partir de la clase
objeto = Calculadora()

# Llamadas a los métodos del objeto
print(objeto.multiplicar(4,5))
print(objeto.dividir(4,5))

print(dir(operaciones))
print(dir(objeto))