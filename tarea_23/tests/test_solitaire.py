import pytest
from src.solitaire import Solitaire


@pytest.fixture()
def solitaire():
    solitaire = Solitaire()
    return solitaire


def test_encrypt_with_blank_key(solitaire):
    output = solitaire.encrypt("DO NOT USE PC", "")
    assert output == "OSKJJ JGTMW"


def test_decrypt_with_blank_key(solitaire):
    output = solitaire.decrypt("OSKJJ JGTMW", "")
    assert output == "DONOT USEPC"


# implementación del cifrado
def tests_letters_to_numbers(solitaire):
    # output = solitaire.letters_to_numbers("DONOTUSEPC")
    # assert output == [4, 15, 14, 15, 20, 21, 19, 5, 16, 3]
    output = solitaire.letters_to_numbers("KDWUPONOWT")
    assert output == [11, 4, 23, 21, 16, 15, 14, 15, 23, 20]


def test_letter_to_number(solitaire):
    output = solitaire.letter_to_number("A")
    assert output == 1


def test_numbers_to_letters(solitaire):
    output = solitaire.numbers_to_letters([15, 19, 11, 10, 10, 10, 7, 20, 13, 23])
    assert output == "OSKJJJGTMW"


def test_number_to_letter(solitaire):
    output = solitaire.number_to_letter(26)
    assert output == "Z"


def test_group_in_five_input_text_without_x(solitaire):
    output = solitaire.group_in_five("DO NOT USE PC")
    assert output == "DONOT USEPC"


def test_group_in_five_input_text_with_x(solitaire):
    output = solitaire.group_in_five("USE  A DECK")
    assert output == "USEAD ECKXX"


def tests_generate_stream(solitaire):
    output = solitaire.generate_stream("DONOTUSEPC", "")
    assert output == "KDWUPONOWT"


def test_add_mod26(solitaire):
    output = solitaire.add_mod26([4, 15, 14, 15, 20, 21, 19, 5, 16, 3], [11, 4, 23, 21, 16, 15, 14, 15, 23, 20])
    assert output == [15, 19, 11, 10, 10, 10, 7, 20, 13, 23]


def test_sub_mod26(solitaire):
    output = solitaire.substract_mod26([15, 19, 11, 10, 10, 10, 7, 20, 13, 23], [11, 4, 23, 21, 16, 15, 14, 15, 23, 20])
    assert output == [4, 15, 14, 15, 20, 21, 19, 5, 16, 3]
