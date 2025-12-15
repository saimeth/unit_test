class Bateria:
    def __init__(self, capacidad):
        self.capacidad = capacidad  # en mAh
        self.nivel = capacidad     # nivel actual de carga

    def usar(self, consumo):
        if consumo > self.nivel:
            self.nivel = 0
        else:
            self.nivel -= consumo
        return self.nivel

    def cargar(self):
        self.nivel = self.capacidad
        return self.nivel

class Telefono:
    def __init__(self, modelo, bateria):
        self.modelo = modelo
        self.bateria = bateria

    def llamar(self, minutos):
        consumo = minutos * 10  # cada minuto consume 10 mAh
        return self.bateria.usar(consumo)

    def cargar_telefono(self):
        return self.bateria.cargar()
