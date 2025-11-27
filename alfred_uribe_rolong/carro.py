class Llanta:
    def __init__(self, tamaño, tipo):
        self.tamaño = tamaño
        self.tipo = tipo

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.llantas = []

    def agregar_llanta(self, llanta: Llanta):
        if isinstance(llanta, Llanta):
           self.llantas.append(llanta)
