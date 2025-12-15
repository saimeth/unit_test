class Motor:
    def __init__(self, tipo: str, potencia: int):
        self.tipo = tipo
        self.potencia = potencia

    def descripcion(self):
        return f"Motor(tipo = {self.tipo}, potencia = {self.potencia}CV)"

class Carro:
    def __init__(self, marca: str, modelo: str, motor: Motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def descripcion(self):
        return f"Carro(marca = {self.marca}, modelo = {self.modelo}, {self.motor.descripcion()})"
        