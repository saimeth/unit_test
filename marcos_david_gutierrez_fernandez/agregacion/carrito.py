from producto import Producto

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise ValueError("Debe ser un producto válido")

        self.productos.append(producto)
    
    def totalPrecio(self):
        total = 0
        for producto in self.productos:
            total = total + producto.precio
        return total
