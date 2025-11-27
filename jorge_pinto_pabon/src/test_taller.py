import pytest 
from taller import Carro, Llanta


def test_llanta_es_instancia():
    llanta = Llanta('invierno', '16 pulgadas')
    assert isinstance(llanta, Llanta)

def test_para_validar_si_permite_agregar_carroas_a_la_clase():
    carro = Carro('Corrola', 'Toyota', 2020)
    assert len (carro.llantas) == 0
    llanta1 = Llanta ('deportiva', '19 pulgadas')
    carro.add_llanta(llanta1)
    assert len (carro.llantas) == 1



def test_atributos_carro_y_llanta():
    llanta = Llanta('todo terreno', '17 pulgadas')
    assert llanta.tipo == 'todo terreno'
    assert llanta.tamanio == '17 pulgadas'
    carro = Carro('Corolla', 'Toyota', 2020)
    assert carro.modelo == 'Corolla'
    assert carro.marca == 'Toyota'
    assert carro.anio == 2020
    assert carro.llantas == []
