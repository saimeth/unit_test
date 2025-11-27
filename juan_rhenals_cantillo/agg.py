class Rueda:
    def __init__(self, tamano: str, tipo: str):
        self.tamano = tamano
        self.tipo = tipo


class VehiculoAgregado:
    def __init__(self, marca: str, modelo: str, anno: int):
        self.marca = marca
        self.modelo = modelo
        self.anno = anno
        self.ruedas = []   

    def add_rueda(self, rueda: Rueda):
        self.ruedas.append(rueda)





