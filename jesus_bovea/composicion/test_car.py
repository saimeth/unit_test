from car import Motor, Carro

def test_atributos():
    motor = Motor("V8", 450)
    auto = Carro("Ford", "Mustang", motor)

    assert auto.motor == motor   
    assert auto.marca == "Ford"
    assert auto.modelo == "Mustang"
    assert auto.motor.tipo == "V8"
    assert auto.motor.potencia == 450


def test_descripcion():
    motor = Motor("V6", 350)
    auto = Carro("Chevrolet", "Camaro", motor)

    descripcion_esperada_motor = "Motor(tipo = V6, potencia = 350CV)"
    descripcion_esperada_carro = f"Carro(marca = Chevrolet, modelo = Camaro, {descripcion_esperada_motor})"

    assert motor.descripcion() == descripcion_esperada_motor
    assert auto.descripcion() == descripcion_esperada_carro

def test_verificar_tipo():
    motor = Motor("Eléctrico", 200)
    auto = Carro("Tesla", "Model 3", motor)

    assert isinstance(auto.motor, Motor)
    assert isinstance(auto.motor.tipo, str)
    assert isinstance(auto.motor.potencia, int)
    assert isinstance(auto.marca, str)
    assert isinstance(auto.modelo, str)

    