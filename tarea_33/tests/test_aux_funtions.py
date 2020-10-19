import pytest

from aux_functions import get_correct_attack_value


def test_get_correct_attack_value_raise_error():
    with pytest.raises(Exception) as e:
        assert get_correct_attack_value("pikachu")
        assert str(e.value) == "El valor debe ser un número entero."


def test_get_correct_attack_value_range_up():
    with pytest.raises(Exception) as e:
        assert get_correct_attack_value(105)
        assert str(e.value) == "El valor debe estar comprendido entre 1 y 100 ambos incluidos."


def test_get_correct_attack_value_range_down():
    with pytest.raises(Exception) as e:
        assert get_correct_attack_value(-5)
        assert str(e.value) == "El valor debe estar comprendido entre 1 y 100 ambos incluidos."
