class ErrorRegistro(Exception):
    pass

class NombreInvalido(ErrorRegistro):
    pass

class EdadInvalida(ErrorRegistro):
    pass

class EmailInvalido(ErrorRegistro):
    pass

def validar_nombre(nombre):
    if nombre.strip() == "":
        raise NombreInvalido("El nombre no puede estar vacío")

def validar_edad(edad):
    if edad <= 0:
        raise EdadInvalida("La edad debe ser mayor a 0")

def validar_email(email):
    if "@" not in email:
        raise EmailInvalido("El email debe contener @")

try:
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    email = input("Ingrese email: ")

    validar_nombre(nombre)
    validar_edad(edad)
    validar_email(email)

    print("Usuario registrado correctamente")

except NombreInvalido as e:
    print("Error de nombre:", e)
except EdadInvalida as e:
    print("Error de edad:", e)
except EmailInvalido as e:
    print("Error de email:", e)
except ValueError:
    print("La edad debe ser un número")
finally:
    print("Fin del proceso de registro")
