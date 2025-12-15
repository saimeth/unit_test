
from celular import Aplicacion, Celular

def test_instancia_celular():
    App01 = Aplicacion("Juego", "clash of honor", "250MB")
    Celular01 = Celular("Samsung", "Galaxy S01", 1000000)
    assert isinstance(App01, Aplicacion)
    assert isinstance(Celular01, Celular)

def test_atributos_celular():
    App02 = Aplicacion("Educativo", "Diccionario", "10mb")
    Celular02 = Celular("Xiaomi", "Redmi 12", 1500000)
    assert App02.tipo == "Educativo"
    assert App02.nombre == "Diccionario"
    assert App02.peso == "10mb"
    assert Celular02.marca == "Xiaomi"
    assert Celular02.modelo == "Redmi 12"
    assert Celular02.precio == 1500000

def test_metodo_celular():
    App03 = Aplicacion("Reproductor musica", "7MUSIC", "11mb")
    App04 = Aplicacion("Reproductor video", "YOUVIDEO", "5mb")
    Celular03 = Celular("Samsung", "J20", 2000000)
    assert len(Celular03.aplicaciones) == 0

    Celular03.instalar_aplicacion(App03)
    Celular03.instalar_aplicacion(App04)

    assert len(Celular03.aplicaciones) == 2
