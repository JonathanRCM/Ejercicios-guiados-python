class Persona:
    nombre = ""
    edad = ""
    curp = ""

    def __init__(self, nom, ed, curp):
        self.nombre = nom
        self.edad = ed
        self.curp = curp

    def mostrarDatos(self):
        print(f'Hola {self.nombre} tienes {self.edad} años y tu curp es: {self.curp}')


objetoPersona = Persona('Jonathan', 18, 'CURP')
objetoPersona.mostrarDatos()