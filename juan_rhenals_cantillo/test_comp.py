from comp import Motor, VehiculoCompuesto

def test_composicion_instancias():
    motor = Motor(120, "Gasolina")
    coche = VehiculoCompuesto("Honda", "Civic", 2022, motor)
    assert isinstance(coche.motor, Motor)

def test_composicion_metodo_aumentar_hp():
    motor = Motor(120, "Gasolina")
    coche = VehiculoCompuesto("Ford", "Fiesta", 2020, motor)
    coche.aumentar_hp(30)
    assert coche.motor.hp == 150  

def test_composicion_atributos_motor():
    motor = Motor(120, "Gasolina")
    coche = VehiculoCompuesto("Nissan", "Versa", 2021, motor)
    assert coche.motor.hp == 120
    assert coche.motor.tipo == "Gasolina"


