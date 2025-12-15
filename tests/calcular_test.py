
from calculator import Carro, Llanta

# Pruebas para la agregación Carro y Llanta
def test_instancia_llanta():
    llanta = Llanta("Michelin", 16)
    assert llanta.marca == "Michelin"
    assert llanta.diametro == 16

def test_instancia_carro():
    carro = Carro("Sedan")
    assert carro.modelo == "Sedan"
    assert carro.cantidad_llantas() == 0

def test_agregar_llantas_al_carro():
    carro = Carro("SUV")
    l1 = Llanta("Pirelli", 18)
    l2 = Llanta("Goodyear", 18)
    carro.agregar_llanta(l1)
    carro.agregar_llanta(l2)
    assert carro.cantidad_llantas() == 2
    assert carro.llantas[0].marca == "Pirelli"
    assert carro.llantas[1].marca == "Goodyear"
    