class Persona:
    def __init__(self,nombre,edad):
     self.nombre = nombre
     self.edad = edad

    def saludarPersona(self):
        print("Hola,mi nombre es " +self.nombre+ " y tengo " +str(self.edad)+ " años ")

person = Persona("Jonathan",18)
person.saludarPersona()


