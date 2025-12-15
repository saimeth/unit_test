class Pantalla:
    def __init__(self, tamaño, tipo):
        if not isinstance(tamaño, int) or tamaño <= 10:
            raise ValueError("tamaño incorrecto")
        if not isinstance(tipo, str):
            raise ValueError("tipo incorrecto")

        self.tamaño = tamaño
        self.tipo = tipo
