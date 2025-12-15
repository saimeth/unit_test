class Llanta:
    def __init__(self, marca, diametro):
        self.marca = marca
        self.diametro = diametro  # en pulgadas

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.llantas = []  # lista de llantas

    def agregar_llanta(self, llanta):
        self.llantas.append(llanta)

    def cantidad_llantas(self):
        return len(self.llantas)
