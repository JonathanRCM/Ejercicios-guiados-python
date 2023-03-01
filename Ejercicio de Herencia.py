class Empleado(object):
  # Constructor de la clase
  def __init__(self,nombre,iden):
    self.nombre = nombre
    self.iden = iden
class RecHumanos(Empleado):
  def saludo(self):
    print("Hola, mi nombre es " + self.nombre + " y mi ID es " + self.iden + ".")
    print("Trabajo en Recursos Humanos.")
