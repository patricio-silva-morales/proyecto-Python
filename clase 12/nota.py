class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    # def esta_aprobado(nota):
    #    return nota >= 4.0
    
    def esta_aprobado(x):
        return x.nota >= 4
    
    
a1 = Alumno("Macarena", 5.7)
print(Alumno.esta_aprobado(a1))