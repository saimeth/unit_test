from carro import Carro, Motor
from carro import Ambiente, Aprendiz

########################### AGREGACIÓN ##################################

# verificar instancia
def test_instancia():
    apren1 = Aprendiz("Manuel")
    apren2 = Aprendiz("Alejandro")
    apren3 = Aprendiz("Sam")

    ambiente = Ambiente("segundo", 30)
    assert len(ambiente.aprendices) == 0

    ambiente.agregarApren(apren1)
    ambiente.agregarApren(apren2)
    ambiente.agregarApren(apren3)

    assert len(ambiente.aprendices) == 3
    assert all(isinstance(a, Aprendiz) for a in ambiente.aprendices)
    assert isinstance(ambiente, Ambiente)


# verificar método agregar
def test_metodo_agregar():
    aprendiz = Aprendiz("Criss")
    ambiente = Ambiente("segundo", 30)

    ambiente.agregarApren(aprendiz)
    assert aprendiz in ambiente.aprendices


# verificar atributos
def test_atributos_ambiente():
    aprendiz = Aprendiz("sam")
    ambiente = Ambiente("segundo", 30)

    assert aprendiz.nombre == "sam"
    assert ambiente.grado == "segundo"
    assert ambiente.silla == 30
    assert ambiente.aprendices == []

    ambiente.agregarApren(aprendiz)
    assert ambiente.aprendices[0].nombre == "sam"








############################## COMPISICIÓN ###############################
## Verificar instancia
def test_carro():
    motor = Motor("ABC12")
    carro1 = Carro(motor, "azul") 
    assert isinstance(carro1, Carro)
    assert isinstance(motor, Motor)


## verificar atributos
def test_atributos1():
    motor = Motor("ABC123")
    carro = Carro(motor, "azul")

    assert carro.color == "azul"
    assert isinstance(carro.motor, Motor)
    assert carro.motor.numSerie == "ABC123"


## verificar método

def test_arrancar():
    motor = Motor("ABC123")
    carro = Carro(motor, "azul")

    resultado = carro.arrancar()

    assert resultado == "El carro de color azul está arrancando con motor ABC123"