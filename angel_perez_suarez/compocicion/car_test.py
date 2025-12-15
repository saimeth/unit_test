import sys
import os

# Agregamos la carpeta src al PATH si tus archivos están allí
sys.path.append(os.path.abspath("src"))

from carro import Coche
from motor import Motor  

# --------------------
# Test de instancia
# --------------------
def test_instancia_coche():
    motor1 = Motor(120)
    coche = Coche("Toyota", motor1)
    # Verificamos que el coche usa el mismo objeto motor
    assert coche.motor is motor1

# --------------------
# Test de atributos
# --------------------
def test_atributos_coche():
    motor1 = Motor(150)
    coche = Coche("Honda", motor1)
    # Verificamos la marca del coche
    assert coche.marca == "Honda"
    # Verificamos la potencia del motor
    assert coche.motor.potencia == 150

# --------------------
# Test de métodos
# --------------------
def test_arrancar_coche():
    motor1 = Motor(120)
    coche = Coche("Toyota", motor1)
    coche.arrancar()
    # Verificamos que el coche está encendido
    assert coche.esta_encendido() is True

def test_apagar_coche():
    motor1 = Motor(120)
    coche = Coche("Toyota", motor1)
    coche.arrancar()
    coche.apagar()
    # Verificamos que el coche está apagado
    assert coche.esta_encendido() is False
