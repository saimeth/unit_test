import pytest
from carro import Carro, Llanta
from persona import Persona, Corazon
# -------------test Carro y Llanta--------------------

def test_validar_existencia_attributos():
    llanta = Llanta("17 pulgadas", "todo terreno")
    assert llanta.tamaño == "17 pulgadas"
    assert llanta.tipo == "todo terreno"

def test_agregar_llantas_al_carro():
    carro = Carro("Camaro", "Chevrolet", 2023)
    llanta1 = Llanta("19 pulgadas", "deportiva")
    llanta2 = Llanta("19 pulgadas", "deportiva")
    llanta3 = Llanta("19 pulgadas", "deportiva")
    llanta4 = Llanta("19 pulgadas", "deportiva")

    carro.agregar_llanta(llanta1)
    carro.agregar_llanta(llanta2)
    carro.agregar_llanta(llanta3)
    carro.agregar_llanta(llanta4)

    assert len(carro.llantas) == 4
    for llanta in carro.llantas:
        assert llanta.tamaño == "19 pulgadas"
        assert llanta.tipo == "deportiva"

def test_agregar_llanta_invalida():
    carro = Carro("Mazda 3", "Mazda", 2022)
    assert isinstance(carro, Carro)
    with pytest.raises(TypeError) as mierror:
        carro.agregar_llanta("esto no es una llanta")
    assert str(mierror.value) == "Solo puedes agregar de tipo Llanta"

# -------------test Persona--------------------
def test_persona_tiene_corazon():
    corazon = Corazon(70)
    p = Persona("cesar", 20, corazon)
    assert isinstance(p.corazon, Corazon)
    assert p.corazon.ritmo == 70
    assert p.corazon.latir() == "El corazón late a 70 bpm" 

def test_persona_saluda():
    p = Persona("cesar", 20)
    resultado = p.saludar()
    assert resultado == "Hola, soy cesar"

def test_persona_edad():
    p = Persona("cesar", 20)
    assert p.edad == 20
