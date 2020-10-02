import pytest
from src.solitaire import Solitaire


@pytest.fixture()
def solitaire():
    solitaire = Solitaire()
    return solitaire


def test_encrypt_with_blank_key(solitaire):
    output = solitaire.encrypt("DO NOT USE PC", "")
    assert output == "HLXMB TKKTJ"
    # output = solitaire.encrypt("AAAAA AAAAA", "")
    # assert output == "EXKYI ZSGEH"


def test_encrypt(solitaire):
    # output = solitaire.encrypt("AAAAA AAAAA AAAAA", "FOO")
    # assert output == "ITHZU JIWGR FARMW"
    # output = solitaire.encrypt("AAAAA AAAAA AAAAA", "F")
    # assert output == "XYIUQ BMHKK JBEGY"
    # output = solitaire.encrypt("AAAAA AAAAA AAAAA", "A")
    # assert output == "XODAL GSCUL IQNSC"
    # output = solitaire.encrypt("AAAAA AAAAA AAAAA AAAAA AAAAA", "CRYPTONOMICON")
    # assert output == "SUGSR SXSWQ RMXOH IPBFP XARYQ"
    output = solitaire.encrypt("SOLITAIRE", "CRYPTONOMICON")
    assert output == "KIRAK SFJAN"


def test_decrypt(solitaire):
    # output = solitaire.decrypt("HLXMB TKKTJ", "")
    # assert output == "DONOTUSEPC"
    # output = solitaire.decrypt("ITHZU JIWGR FARMW", "FOO")
    # assert output == "AAAAAAAAAAAAAAA"
    # output = solitaire.decrypt("XYIUQ BMHKK JBEGY", "F")
    # assert output == "AAAAAAAAAAAAAAA"
    output = solitaire.decrypt("KIRAK SFJAN", "CRYPTONOMICON")
    assert output == "SOLITAIREX"
    # output = solitaire.decrypt("HBCNC DKARI OFVIC DISQH", "")
    # assert output == "DESPUESUNBUSCAMINASX"


# implementación del cifrado
def tests_letters_to_numbers(solitaire):
    output = solitaire.letters_to_numbers("DONOTUSEPC")
    assert output == [4, 15, 14, 15, 20, 21, 19, 5, 16, 3]
    # output = solitaire.letters_to_numbers("KDWUPONOWT")
    # output = solitaire.letters_to_numbers("XKYIZSGEH")
    # assert output == [11, 4, 23, 21, 16, 15, 14, 15, 23, 20]


def test_letter_to_number(solitaire):
    output = solitaire.letter_to_number("A")
    assert output == 1
    output = solitaire.letter_to_number("")
    assert output == 0


def test_numbers_to_letters(solitaire):
    output = solitaire.numbers_to_letters([15, 19, 11, 10, 10, 10, 7, 20, 13, 23])
    assert output == "OSKJJJGTMW"
    # assert output == "EXKYIZSGEH"


def test_number_to_letter(solitaire):
    output = solitaire.number_to_letter(26)
    assert output == "Z"


def test_group_in_five_input_text_without_x(solitaire):
    output = solitaire.group_in_five("DO NOT USE PC")
    assert output == "DONOT USEPC"


def test_complete_with_x(solitaire):
    output = solitaire.complete_with_x("USEADECK")
    assert output == "USEADECKXX"
    output = solitaire.complete_with_x("SOLITAIRE")
    assert output == "SOLITAIREX"


def tests_generate_stream(solitaire):
    output = solitaire.generate_stream("DONOTUSEPC", "")
    assert output == "DWJXHYRFDG"


def test_add_mod26(solitaire):
    output = solitaire.add_mod26([4, 15, 14, 15, 20, 21, 19, 5, 16, 3], [11, 4, 23, 21, 16, 15, 14, 15, 23, 20])
    assert output == [15, 19, 11, 10, 10, 10, 7, 20, 13, 23]


def test_sub_mod26(solitaire):
    output = solitaire.substract_mod26([15, 19, 11, 10, 10, 10, 7, 20, 13, 23], [11, 4, 23, 21, 16, 15, 14, 15, 23, 20])
    assert output == [4, 15, 14, 15, 20, 21, 19, 5, 16, 3]
