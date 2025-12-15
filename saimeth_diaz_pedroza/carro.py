class Motor:
    def __init__(self, numSerie):
        self.numSerie = numSerie

class Carro:
    def __init__(self, motor, color):
        self.color = color
        if isinstance(motor, Motor):
            self.motor = motor

    def arrancar(self):
        return f"El carro de color {self.color} está arrancando con motor {self.motor.numSerie}"




##agregación
class Aprendiz:
    def __init__(self, nombre):
        self.nombre = nombre


class Ambiente:
    def __init__ (self, grado, silla):
        self.grado = grado
        self.silla = silla
        self.aprendices=[]

    def agregarApren(self, aprendiz):
        if isinstance(aprendiz, Aprendiz):
            self.aprendices.append(aprendiz)