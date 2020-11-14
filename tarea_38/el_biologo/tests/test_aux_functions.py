import pytest

from aux_functions import chek_dna_sequence

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
