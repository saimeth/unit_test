from motor import Motor

class Coche:
    def __init__(self, marca, motor):
        # Composición: el coche crea su propio motor
        self.marca = marca
        self.motor = motor

    def arrancar(self):
        self.motor.encender()

    def apagar(self):
        self.motor.apagar()

    def esta_encendido(self):
        return self.motor.encendido
