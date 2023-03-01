#Se utiliza el constructor para pedir los datos, como ves el constructor no tiene que ser llamado se invoca solito
# cuando creamos la instancia de la clase.
class Persona:
    nombre = ""
    edad = ""
    curp = ""

    def __init__(self):
        self.nombre = input('Ingrese su nombre ')
        self.edad = int(input('Ingrese su edad: '))
        self.curp = input('Ingrese su curp: ')

    def mostrarDatos(self):
        print(f'Hola {self.nombre} tienes {self.edad} años y tu curp es: {self.curp}')


objetoPersona = Persona()
objetoPersona.mostrarDatos()