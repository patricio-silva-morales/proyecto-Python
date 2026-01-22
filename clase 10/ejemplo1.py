def bienvenida():
    print("Bienvenido a la aplicación SaludosApp")    

# Definición de la función saludo_sin_retorno()
# Se ha definido un parámetro: nombre
def saludo_sin_retorno(nombre):
    # Cuerpo de la función
    print(f"Hola! Buenos días, {nombre}! Espero que esté bien")
    
def saludo_con_retorno(nombre):
    # Cuerpo de la función
    return "Hola! Buenos días, " + nombre + "! Espero que esté bien"
    
def despedida():
    print("Gracias por usar la aplicación. Nos vemos!")

# Programa principal
# Llamada a las funciones
bienvenida()
saludo_sin_retorno("Manuel")
print(saludo_con_retorno("Pedro"))
despedida()