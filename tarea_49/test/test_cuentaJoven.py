import pytest
from persona import Persona
from cuentaJoven import CuentaJoven

@pytest.fixture()
def cuenta_joven():
    titular = Persona("Maria", 25, "30123456B")
    cuenta_joven = CuentaJoven(titular)
    return cuenta_joven


def test_cuenta_joven_sin_titular_lanza_excepcion():
    with pytest.raises(TypeError) as te:
        cuenta_joven = CuentaJoven()
        assert str(te.value == "__init__() missing 1 required positional argument: 'titular'")


def test_cuenta_joven_sin_bonificacion(cuenta_joven):
    output = cuenta_joven.mostrar()
    assert output == "Cuenta Joven:\n - Titular: Nombre: Maria - Edad: 25 - DNI: 30123456B \n - Cantidad: 0 \n - " \
                     "Bonificación: 0 %"


test_data_titular_invalido = [8, 15, 25, 55, 68]
test_data_titular_valido = [18, 19, 20, 21, 22, 23, 24]


@pytest.mark.parametrize("edad", test_data_titular_valido)
def test_es_titular_valido(cuenta_joven, edad):
    cuenta_joven.titular.edad = edad
    assert cuenta_joven.es_titular_valido() is True


@pytest.mark.parametrize("edad", test_data_titular_invalido)
def test_es_titular_invalido(cuenta_joven, edad):
    cuenta_joven.titular.edad = edad
    assert cuenta_joven.es_titular_valido() is False


def test_retirar_titular_invalido_lanza_excepcion(cuenta_joven):
    with pytest.raises(ValueError) as ve:
        cuenta_joven.retirar(5)
        assert str(ve.value == "El titular no es válido. No puede retirar dinero de la cuenta")
