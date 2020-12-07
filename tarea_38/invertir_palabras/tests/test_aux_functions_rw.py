import pytest
from aux_functions_rw import get_non_negative_int, get_correct_sentence


def test_get_non_negative_int_raise_error():
    with pytest.raises(Exception) as e:
        assert get_non_negative_int('\n')
        assert str(e.value) == "El valor debe ser un número entero."


def test_get_non_negative_int():
    with pytest.raises(Exception) as e:
        assert get_non_negative_int(-5)
        assert str(e.value) == "El valor no puede ser negativo."


def test_get_correct_sentence_raise_error():
    with pytest.raises(Exception) as e:
        assert get_correct_sentence('\n')
        assert str(e.value) == "El valor debe ser una cadena de texto"


def test_get_correct_sentence_raise_error_with_a_number():
    with pytest.raises(Exception) as e:
        assert get_correct_sentence("foobar 4")
        assert get_correct_sentence("this  is")
        assert str(
            e.value) == "El texto de entrada debe estar compuesto sólo por caracteres de texto separados por un único " \
                        "espacio en blanco "


def test_get_correct_sentence_raise_error_with_two_espaces():
    with pytest.raises(Exception) as e:
        assert get_correct_sentence("this  is")
        assert str(
            e.value) == "El texto de entrada debe estar compuesto sólo por caracteres de texto separados por un único " \
                        "espacio en blanco "
