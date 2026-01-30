class Usuario:
    
    def saludar(self):
        print("¡Buenos días!")
    
class Administrador(Usuario):
    
    def acceder_panel(self):
        print("Accediendo a panel...")
        
class Cliente(Usuario):
    
    def realizar_compra(self):
        print("Realizando compra...")
        
usuarios = []

usuarios.append(Usuario())
usuarios.append(Administrador())
usuarios.append(Cliente())

for user in usuarios:
    if isinstance(user, Cliente):
        user.realizar_compra()
    elif isinstance(user, Administrador):
        user.acceder_panel()
    elif isinstance(user, Usuario):
        user.saludar()
    else:
        print("No es un tipo reconocible")