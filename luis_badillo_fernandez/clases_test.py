class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []
        
    def add(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
    
    def cantidad(self):
        return len(self.productos)
        

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def encender(self):
        self.encendido = True
        return "motor encendido"
            
        
class Carro:
    def __init__(self, motor, pintura):
        self.motor = motor
        self.pintura = pintura
    
    def arrancar(self):
        
        return self.motor.encender()
    

    
        
        
        

                