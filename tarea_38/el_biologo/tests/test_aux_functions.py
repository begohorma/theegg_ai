import pytest

from aux_functions import chek_dna_sequence, get_correct_dna_sequence

test_data_valid = [
    "CTGACTGA",
    "AACTGAGC",
    "AA",
    "C",
    "GT"
]

test_data_invalid = [
    "CTGJ",
    "AACTZAGC",
    "AAB",
    "YCCATY",
    "GT1",
    ""
]


@pytest.mark.parametrize("seq", test_data_valid)
def test_correct_dna_sequence(seq):
    output = chek_dna_sequence(seq)
    assert output is True


@pytest.mark.parametrize("seq", test_data_invalid)
def test_incorrect_dna_sequence(seq):
    output = chek_dna_sequence(seq)
    assert output is False


def test_get_correct_dna_sequence_raise_error():
    with pytest.raises(Exception) as e:
        assert get_correct_dna_sequence('\n')
        assert str(e.value) == "El valor debe ser una cadena de texto"


def test_get_correct_dna_sequence_valid_characters():
    with pytest.raises(Exception) as e:
        assert get_correct_dna_sequence("ACJGT")
        assert str(e.value) == "La secuencia sólo puede contener los caracteres de las bases A, C, G y T "
