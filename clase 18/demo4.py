def validar_email(email):
    if "@" not in email: # Si el email NO contiene el caracter #
        raise ValueError("Email inválido")
    
def registrar_usuario(email):
    try:
        validar_email(email)
    except ValueError as e:
        print("Error interno:", e) # Primer mensaje de error
        raise RuntimeError("Fallo al registrar usuario") # Implícitamente propaga la excepción ValueError

try:
    registrar_usuario("juanito.com")
except ValueError:
    # Segundo mensaje de error
    print("Error detectado en el sistema externo: Reintenta con un email válido")
except RuntimeError:
    print("Error inseperado en la ejecución")