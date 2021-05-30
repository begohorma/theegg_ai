import pytest
from cuenta import Cuenta
from persona import Persona


@pytest.fixture()
def cuenta():
    titular = Persona("Maria", 25, "30123456B")
    cuenta = Cuenta(titular)
    return cuenta


def test_cuenta_sin_titular_lanza_excepcion():
    with pytest.raises(TypeError) as te:
        cuenta = Cuenta()
        assert str(te.value == "__init__() missing 1 required positional argument: 'titular'")


def test_cuenta_sin_cantidad(cuenta):
    output = cuenta.mostrar()
    assert output == "Datos de la cuenta:\n - Titular: Nombre: Maria - Edad: 25 - DNI: 30123456B \n - Cantidad: 0"


def test_cantidad_no_modificable_directamente(cuenta):
    with pytest.raises(AttributeError) as ae:
        cuenta.cantidad = 33
        assert str(ae.value == "can't set attribute")


def test_ingresar_cantidad_negativa_no_hace_nada(cuenta):
    cantidad_original = cuenta.cantidad
    output = cuenta.ingresar(-25)
    assert cuenta.cantidad == cantidad_original
    assert output == "La cantidad a ingresar es < 0. El saldo de la cuenta de {0} no se modifica".format(cuenta.titular.nombre)


def test_ingresar_cantidad_no_float_lanza_excepcion(cuenta):
    with pytest.raises(TypeError) as te:
        cuenta.ingresar("a")
        assert str(te.value == "'>' not supported between instances of 'str' and 'int'")


def test_ingresar(cuenta):
    cantidad_original = cuenta.cantidad
    output = cuenta.ingresar(23.5)
    assert cuenta.cantidad == cantidad_original + 23.5
    assert output == "Se ha ingresado 23.5 en la cuenta de {0}. El nuevo saldo es: 23.5".format(cuenta.titular.nombre)
    cantidad_original2 = cuenta.cantidad
    output2 = cuenta.ingresar(23.5)
    assert cuenta.cantidad == cantidad_original2 + 23.5
    assert output2 == "Se ha ingresado 23.5 en la cuenta de {0}. El nuevo saldo es: 47.0".format(cuenta.titular.nombre)


def test_retirar_cantidad_mayor_saldo_actual_da_numeros_rojos(cuenta):
    output = cuenta.retirar(50)
    assert output == "Se ha retirado 50 de la cuenta de {0}. La cantidad actual de la cuenta es: -50. ¡¡La cuenta está en Números Rojos!!".format(cuenta.titular.nombre)


def test_retirar(cuenta):
    cuenta.ingresar(60.0)
    output = cuenta.retirar(25)
    assert output == "Se ha retirado 25 de la cuenta de {0}. La cantidad actual de la cuenta es: 35.0".format(cuenta.titular.nombre)
