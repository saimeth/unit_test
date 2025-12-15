from clases_test import Producto, Carrito, Carro, Motor

def test_intancia_ag():
    carrito = Carrito()
    assert isinstance(carrito,Carrito)
    
def test_metodos_ag():
    carrito = Carrito()
    
    producto1 = Producto("pera", 3000)
    producto2 = Producto("manzana", 2500)
    assert len(carrito.productos) == 0
    carrito.add(producto1)
    carrito.add(producto2)
    assert len(carrito.productos) == 2
    assert carrito.cantidad() == 2
    
    
def test_atributos_ag():
    producto1 = Producto("leche", 4500)
    assert producto1.nombre == "leche"
    assert producto1.precio == 4500
    

def test_instancia_comp():
    motor = Motor(1200)
    carro = Carro(motor, "rojo")
    
    assert isinstance(motor, Motor)
    assert isinstance(carro, Carro)
    

def test_metodos_comp():
    motor = Motor(1200)
    carro = Carro(motor, "rojo")
    
    encendido = carro.arrancar()
    
    assert "motor encendido" in encendido

def test_atributos_comp():
    motor = Motor(1200)
    carro = Carro(motor, "rojo")
    
    assert motor.potencia == 1200
    assert carro.pintura == "rojo"