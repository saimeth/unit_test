class Llanta:
    def __init__(self, tipo: str, tamanio: str):
        self.tipo = tipo
        self.tamanio = tamanio


class Carro:
    def __init__(self, modelo: str, marca: str, anio: int):
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.llantas = []
    
    
    def add_llanta (self, llanta: Llanta):
        if not isinstance (llanta, Llanta):
            raise TypeError('El objeto debe ser una llanta')
        self.llantas.append(llanta)