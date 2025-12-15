import pytest
from carrito import Carrito
from producto import Producto

def test_carrito_inicia_vacio():
    carrito = Carrito()
    assert len(carrito.productos) == 0
    p1 = Producto("Queso", 7000)
    p2 = Producto("Leche", 3200)
    p3 = Producto("Huevos", 9000)
    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)
    carrito.agregar_producto(p3)
    assert len(carrito.productos) == 3

def test_varios_productos_validos():
    p1 = Producto("Queso", 5000)
    p2 = Producto("Leche", 3200)
    p3 = Producto("Huevos", 9000)
    assert p1.nombre == "Queso" and p1.precio == 5000
    assert p2.nombre == "Leche" and p2.precio == 3200
    assert p3.nombre == "Huevos" and p3.precio == 9000

def test_precio_invalido():
    with pytest.raises(ValueError) as mensajeError:
        Producto("Pan", "caro")
    assert str(mensajeError.value) == "Precio incorrecto"

def test_nombre_invalido():
    with pytest.raises(ValueError) as mensajeError:
        Producto(123, 1500)
    assert str(mensajeError.value) == "Nombre incorrecto"

def test_agregar_producto_no_valido():
    carrito = Carrito()
    with pytest.raises(ValueError) as mensajeError:
        carrito.agregar_producto("No es un producto")
    assert str(mensajeError.value) == "Debe ser un producto válido"

def test_total():
    carrito = Carrito()
    p1 = Producto("Queso", 7000)
    p2 = Producto("Leche", 3200)
    p3 = Producto("Huevos", 9000)
    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)
    carrito.agregar_producto(p3)
    assert carrito.totalPrecio() == carrito.productos[0].precio + carrito.productos[1].precio + carrito.productos[2].precio