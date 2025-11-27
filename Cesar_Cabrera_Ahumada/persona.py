class Corazon:
    def __init__(self, ritmo = 70):
        self.ritmo = ritmo

    def latir(self):
        return f"El corazón late a {self.ritmo} bpm"


class Persona:
    def __init__(self, nombre, edad, corazon: Corazon = None):
        self.nombre = nombre
        self.edad = edad
        self.corazon = corazon if corazon else Corazon()

    def mostrar_ritmo(self):
        return self.corazon.latir()

    def saludar(self):
        return f"Hola, soy {self.nombre}"
