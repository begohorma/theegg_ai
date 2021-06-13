import pytest
from aux_functions import get_correct_input_string


def test_incorrect_type_of_input_raise_error():
    with pytest.raises(Exception) as e:
        assert get_correct_input_string(345)
        assert str(e.value) == "La entrada debe ser una cadena de texto"


