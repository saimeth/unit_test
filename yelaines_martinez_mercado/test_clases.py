###agregacion###

### verificicar instancias de la lista ###
from clases import Estudiante,Salon
from clases import Carro,Motor

def test_instancias():
    estd1=Estudiante("pablo")
    estd2=Estudiante("gustavo")
    estd3=Estudiante("ana")
    estd4=Estudiante("carlos")
    salon=Salon("Sexto","maria auxiliadora")
    salon.agregarEstudiantes(estd1)
    salon.agregarEstudiantes(estd2)
    salon.agregarEstudiantes(estd3)
    salon.agregarEstudiantes(estd4)
    
    assert all(isinstance(e, Estudiante) for e in salon.estudiantes)
    assert isinstance(salon,Salon)
    



### verificar que el metodo agregue los estudiantes a la lista ###

def test_lista():
    estudiante=Estudiante("gabriel")
    salon=Salon("Sexto","maria auxiliadora")
    salon.agregarEstudiantes(estudiante)
    assert estudiante in salon.estudiantes

### verficar atributos 

def test_atributos():
    salon=Salon("Sexto","maria auxiliadora")
    assert salon.grado=="Sexto"
    assert salon.colegio=="maria auxiliadora"
    

#### composicion


### verificar instancias de clases
def test_inst():
    motor=Motor("3456FG")
    car=Carro(motor,"4","AZUL","7485HHJ")

    assert isinstance(car,Carro)
    assert isinstance(motor,Motor)
    
def test_atributos_com():
    motor=Motor("384hwhd")
    car=Carro(motor,"4","AZUL","7485HHJ")
    assert isinstance(car.motor,Motor)
    assert motor.numero=="384hwhd"
    assert car.color=="AZUL"
    assert car.llanta=="4"
    assert car.placa=="7485HHJ"
    
def test_metodo_com():
    motor=Motor("384hwhd")
    car=Carro(motor,"4","AZUL","7485HHJ")
    ruido=car.ruidoMotor("ruun")
    assert ruido=="ruun"
    
    
    


