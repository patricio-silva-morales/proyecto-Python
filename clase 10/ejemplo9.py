def validar_password(password):
    if len(password) < 8:
        return False

    tiene_letra = False
    tiene_numero = False
    tiene_mayuscula = False

    for char in password:
        if char.isalpha():
            tiene_letra = True
        if char.isdigit():
            tiene_numero = True
        if char.isupper():
            tiene_mayuscula = True

    return tiene_letra and tiene_numero and tiene_mayuscula

password = input("Ingrese una contraseña para validar: ")
if validar_password(password):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida. Debe tener al menos 8 caracteres, una letra, un número y una letra mayúscula.")