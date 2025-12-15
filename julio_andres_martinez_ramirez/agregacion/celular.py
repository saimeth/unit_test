class Aplicacion:
      def __init__(self, tipo, nombre, peso):
            self.tipo = tipo
            self.nombre = nombre
            self.peso = peso

class Celular:
      def __init__(self, marca, modelo, precio):
            self.marca = marca
            self.modelo = modelo
            self.precio = precio

            self.aplicaciones = []

      def instalar_aplicacion(self, aplicacion):
            self.aplicaciones.append(aplicacion) 