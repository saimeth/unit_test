from calculator_composicion import Telefono, Bateria


# Pruebas unitarias para la composición Teléfono y Batería
def test_bateria_uso_y_carga():
    bateria = Bateria(100)
    assert bateria.nivel == 100
    bateria.usar(30)
    assert bateria.nivel == 70
    bateria.cargar()
    assert bateria.nivel == 100

def test_telefono_llamar_consumo():
    tel = Telefono("Modelo X", 200)
    assert tel.bateria.nivel == 200
    tel.llamar(5) 
    assert tel.bateria.nivel == 150
    tel.llamar(20) 
    assert tel.bateria.nivel == 0

def test_telefono_cargar():
    tel = Telefono("Modelo Y", 120)
    tel.llamar(10)
    assert tel.bateria.nivel < 120
    tel.cargar_telefono()
    assert tel.bateria.nivel == 120

def test_bateria_en_telefono():
    bateria = Bateria(3000)
    telefono = Telefono("Modelo X", bateria)
    assert telefono.bateria == bateria, "La batería no se agregó correctamente al teléfono"
