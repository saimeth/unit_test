class Motor:
    def __init__(self, hp: int, tipo: str):
        self.hp = hp
        self.tipo = tipo

class VehiculoCompuesto:
    def __init__(self, marca: str, modelo: str, anno: int, motor: Motor): 
        self.marca = marca
        self.modelo = modelo
        self.anno = anno
        self.motor = motor  

    def aumentar_hp(self, cantidad: int):
        self.motor.hp += cantidad
