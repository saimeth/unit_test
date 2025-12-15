from house import Mueble,Casa

def test_atributos():
    silla = Mueble("Silla")
    sofaCama = Mueble("SofaCama")
    casa = Casa("Carrera 38 # 27c-203")

    
    assert casa.direccion == "Carrera 38 # 27c-203"
    assert silla.tipo == "Silla"
    assert sofaCama.tipo == "SofaCama"
    

def test_agregar_muebles():
    silla = Mueble("Silla")
    sofaCama = Mueble("SofaCama")
    casa = Casa("Carrera 38 # 27c-203")

    assert len(casa.muebles) == 0

    casa.agregarMueble(silla)
    casa.agregarMueble(sofaCama)

    assert len(casa.muebles) == 2
    assert casa.muebles[0] is silla
    assert casa.muebles[1] is sofaCama

def test_tipo_atributos():
    silla = Mueble("Silla")
    sofaCama = Mueble("SofaCama")
    casa = Casa("Carrera 38 # 27c-203")

    casa.agregarMueble(silla)
    casa.agregarMueble(sofaCama)

    assert isinstance(silla.tipo, str)
    assert isinstance(sofaCama.tipo, str)
    assert isinstance(casa.direccion, str)
    for x in casa.muebles:
        assert isinstance(x,Mueble)