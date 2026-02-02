class ErrorAplicacion(Exception):
    pass

class ErrorValidacion(ErrorAplicacion):
    pass

class ErrorPermisos(ErrorAplicacion):
    pass

def verificar_usuario(rol):
    if rol == "visitante":
        raise ErrorPermisos("Acceso no autorizado")
    elif rol not in ["admin", "editor"]:
        raise ErrorValidacion("Rol inválido")
    
try:
    verificar_usuario("visitante")
    
except ErrorPermisos as e:
    print(e) # Mensaje predefinido
    # print("Error: No tienes permisos suficientes") # Mensaje personalizado
except ErrorValidacion:
    print("Error: Datos inválidos")
except ErrorAplicacion:
    print("Error: Otro error general de aplicación")