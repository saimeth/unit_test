from pantalla import Pantalla

class Telefono:
    def __init__(self, numero, tipo, pantalla):
        self.numero = numero
        self.tipo = tipo
        if not isinstance(pantalla, Pantalla):
            raise ValueError("Pantalla inválida")

        self.pantalla = pantalla
