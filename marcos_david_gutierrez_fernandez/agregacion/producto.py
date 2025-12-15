class Producto:
    def __init__(self, nombre, precio):
        if not isinstance(nombre, str):
            raise ValueError("Nombre incorrecto")

        if not isinstance(precio, (int, float)):
            raise ValueError("Precio incorrecto")

        self.nombre = nombre
        self.precio = precio
