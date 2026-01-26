class Docente:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad


class Curso:
    def __init__(self, nombre, nombre_docente, especialidad_docente):
        self.nombre = nombre
        self.docente = Docente(nombre_docente, especialidad_docente)

    def mostrar_info(self):
        print("Curso:", self.nombre)
        print("Docente:", self.docente.nombre)
        print("Especialidad:", self.docente.especialidad)


class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cursos = []

    def inscribirse(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        for curso in self.cursos:
            print(curso.nombre)


curso1 = Curso("Excel", "Ana", "Ofimática")
curso2 = Curso("Bootcamp Python", "Carlos", "Programación")

alumno1 = Alumno("Lucía", 20)
alumno1.inscribirse(curso1)
alumno1.inscribirse(curso2)

curso1.mostrar_info()

alumno1.mostrar_cursos()