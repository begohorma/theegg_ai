import pytest
from persona import Persona


@pytest.fixture()
def persona():
    persona = Persona()
    return persona


def test_persona_con_atributos_vacios(persona):
    output = persona.mostrar()
    assert output == "Nombre:  - Edad: 0 - DNI: "


def test_edad_menor_cero_lanza_expcepcion(persona):
    with pytest.raises(ValueError) as ve:
        persona.edad = -1
        assert str(ve.value == "La edad debe ser un valor entero mayor que 0 ")


def test_edad_no_entero_lanza_expcepcion(persona):
    with pytest.raises(ValueError) as ve:
        persona.edad = "a"
        assert str(ve.value == "La edad debe ser un valor entero mayor que 0 ")


test_data_mayor_edad = [18, 22, 55, 68]
test_data_menor_edad = [8, 10, 15, 17]


@pytest.mark.parametrize("edad", test_data_mayor_edad)
def test_es_mayor_de_edad(persona, edad):
    persona.edad = edad
    assert persona.es_mayor_de_edad() is True


@pytest.mark.parametrize("edad", test_data_menor_edad)
def test_es_menor_de_edad(persona, edad):
    persona.edad = edad
    assert persona.es_mayor_de_edad() is False


test_data_incorrect_dni = ["A123", "123456789", "123A5678B", "1234567AB"]


@pytest.mark.parametrize("dni", test_data_incorrect_dni)
def test_dni_estructura_incorrecta_lanza_excepcion(persona, dni):
    with pytest.raises(ValueError) as ve:
        persona.dni = dni
        assert str(ve.value == "La estructura del Dni no es correcta. Debe tener 8 dígitos seguidos de una letra.")


test_data_incorrect_dni_letter = ["30123456A", "30123456K", "30123456Z"]


@pytest.mark.parametrize("dni", test_data_incorrect_dni_letter)
def test_dni_letra_incorrecta_lanza_excepcion(persona, dni):
    with pytest.raises(ValueError) as ve:
        persona.dni = dni
        assert str(ve.value == "La letra del DNI " + dni + " no es correcta")


def test_dni_correcto(persona):
    persona.dni = "30123456B"
    assert persona.mostrar() == "Nombre:  - Edad: 0 - DNI: 30123456B"
