class Corazon:
    def __init__(self, ritmo):
        self.ritmo = 0

    def latir(self):
        self.ritmo += 1


class Humano:
    def __init__(self, raza, sexo, corazon: Corazon = None):
        self.raza = raza
        self.sexo = sexo
        self.corazon = corazon if corazon else Corazon(0)
