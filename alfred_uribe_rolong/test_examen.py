from casa import Casa, Habitacion
from carro import Carro, Llanta

#composicion

def test_instancia_casa():
    hab = Habitacion("Sala", 20)
    casa = Casa("Calle 123", hab)
    assert isinstance(casa, Casa)

def test_atributo_habitacion():
    hab = Habitacion("Dormitorio", 12)
    assert hab.nombre == "Dormitorio"
    assert hab.metros == 12

def test_casa_tiene_una_habitacion():
    hab = Habitacion("Cocina", 11)
    casa = Casa("Calle 123", hab)

    assert isinstance(casa.habitacion, Habitacion)
    assert casa.habitacion.nombre == "Cocina"
    assert casa.habitacion.metros == 11


#agregacion

def test_atributo():
    carro = Carro("Mazda 3")
    assert carro.modelo == "Mazda 3"


def test_agregar_llantas():
    carro = Carro("Mazda 3")
    l1 = Llanta("20 pulgadas", "deportiva")
    l2 = Llanta("20 pulgadas", "deportiva")

    carro.agregar_llanta(l1)    
    carro.agregar_llanta(l2)

    assert len(carro.llantas) == 2
    assert carro.llantas[0].tamaño == "20 pulgadas"


def test_instancia():
    carro = Carro("Mazda 3")
    assert isinstance(carro, Carro)



