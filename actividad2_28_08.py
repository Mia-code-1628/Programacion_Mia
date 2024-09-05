class Persona:
    def __init__(self, dni, nombreApellido, direccion):
        self.dni = dni
        self.nombreApellido = nombreApellido
        self.direccion = direccion

    def mostrar_datos(self):
        print("DNI:", self.dni, ", Nombre:", self.nombreApellido, ", Dirección:", self.direccion)

class Estudiante(Persona):
    def __init__(self, dni, nombreApellido, direccion, matricula, unicoCurso, materias):
        super().__init__(dni, nombreApellido, direccion)
        self.matricula = matricula
        self.unicoCurso = unicoCurso
        self.materias = materias

    def mostrar_datos(self):
        Persona.mostrar_datos(self)
        print("Matrícula:", self.matricula, ", Curso único:", self.unicoCurso, ", Materias:", ", ".join(self.materias))

class Docente(Persona):
    def __init__(self, dni, nombreApellido, direccion, cursosAcargo):
        super().__init__(dni, nombreApellido, direccion)
        self.cursosAcargo = cursosAcargo

    def mostrar_datos(self):
        Persona.mostrar_datos(self)
        print("Cursos a Cargo:")
        for curso in self.cursosAcargo:
            print("- " + curso)

estudiante1 = Estudiante("12345678", "Lola Ruiz", "Avenida Malvinas", "E001", "2do Año", ["Lengua", "Fisica"])
estudiante2 = Estudiante("87654321", "Carolina Martinez", "Avenida Join 456", "E002", "1er Año", ["Literatura", "Matematica"])
estudiante3 = Estudiante("11223344", "Jana Romero", "Boulevard 789", "E003", "3er Año", ["Arte", "Club"])

docente1 = Docente("33445566", "Raul Torres", "Calle Marcos San Justo 345", ["Matemáticas", "Física"])
docente2 = Docente("55667788", "Luciana Lopez", "Salida Ruta 2684", ["Historia", "Quimica"])
docente3 = Docente("77889900", "Sofia Salina", "Tucuman 1021", ["Programacion", "Filosofia"])

estudiante1.mostrar_datos()
estudiante2.mostrar_datos()
estudiante3.mostrar_datos()

docente1.mostrar_datos()
docente2.mostrar_datos()
docente3.mostrar_datos()
