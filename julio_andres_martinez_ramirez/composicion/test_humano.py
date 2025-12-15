from humano import Corazon,Humano

def test_instancia_humano():
    corazon01 = Corazon(0)
    humano01 = Humano("Latino", "masculino", corazon01)
    assert isinstance(humano01, Humano)
    assert isinstance(corazon01, Corazon)

def test_atributos_humano():
    Humano02 = Humano("Asiatico", "masculino")
    assert Humano02.raza == "Asiatico"
    assert Humano02.sexo == "masculino"

def test_funcion_corazon():
    Corazon03 = Corazon(0)
    Humano03 = Humano("Europea", "Femenino",Corazon03)
    Humano03.corazon.latir()
    assert Humano03.corazon == Corazon03