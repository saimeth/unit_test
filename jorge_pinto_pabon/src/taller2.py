class Componente:
    def __init__(self, tipo: str, marca: str):
        self.tipo = tipo
        self.marca = marca


class Computadora:
    def __init__(self, modelo: str, marca: str, anio: int, componente: Componente = None):
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.componentes = componente if componente else Componente()
