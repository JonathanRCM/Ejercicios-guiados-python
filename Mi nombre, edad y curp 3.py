#Se crea una clase, se declara tres atributos y dos métodos, luego se instancia un objeto de esa clase y se manda a  llamar a sus métodos,
# el primero se encarga de pedir los datos y el segundo de imprimirlos

class Persona:
    nombre = ""
    edad = ""
    curp = ""

    def pedirDatos(self):
        self.nombre = input('Ingrese su nombre ')
        self.edad = int(input('Ingrese su edad: '))
        self.curp = input('Ingrese su curp: ')

    def mostrarDatos(self):
        print(f'Hola {self.nombre} tienes {self.edad} años y tu curp es: {self.curp}')


objetoPersona = Persona()
objetoPersona.pedirDatos()
objetoPersona.mostrarDatos()