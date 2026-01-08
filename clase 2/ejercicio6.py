nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 18:
    valor = "$1.000"
else: 
    valor = "$4.000"
    
print(f"Hola {nombre}! El valor de la entrada es {valor}")