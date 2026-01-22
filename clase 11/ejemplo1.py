def crear_cliente(nombre, edad):
    return {"nombre": nombre, "edad": edad}

def saludar(cliente):
    print(f"Hola, {cliente['nombre']}")
    
cliente = crear_cliente("Pedro", 20)
saludar(cliente)