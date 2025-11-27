class Llanta:
    def __init__(self, tamanio, tipo):
        self.tamaño = tamanio
        self.tipo = tipo


class Carro:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.llantas = []

    def agregar_llanta(self, llanta: Llanta):
        if not isinstance(llanta, Llanta):
            raise TypeError("Solo puedes agregar de tipo Llanta")
        self.llantas.append(llanta)
