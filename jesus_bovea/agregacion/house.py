class Mueble:
    def __init__(self, tipo: str):
        self.tipo = tipo
    
    def descripcion(self):
        return f"Mueble tipo: {self.tipo}"
    

class Casa:
    def __init__(self, direccion: str):
        self.direccion = direccion
        self.muebles = []

    def agregarMueble(self, mueble: Mueble):
        self.muebles.append(mueble)
    
    def descripcion(self):
        lista_muebles = ", ".join(m.tipo for m in self.muebles)
        return f"La casa de la dirreccion: {self.direccion} tiene {lista_muebles}"


