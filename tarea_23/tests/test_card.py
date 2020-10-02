import pytest
from src.card import Card


@pytest.fixture()
def card():
    card = Card("Clubs", 5)
    return card


def test_get_card_suit(card):
    output = card.get_suit()
    assert output == "Clubs"


def test_get_card_rank(card):
    output = card.get_rank()
    assert output == 5


def test_show_card_as_string(card):
    output = str(card)
    assert output == "5C"


def test_card_to_number(card):
    output = card.card_to_number()
    assert output == 5
    output = Card("Diamonds", 5).card_to_number()
    assert output == 18
    output = Card("Hearts", 5).card_to_number()
    assert output == 31
    output = Card("Spades", 5).card_to_number()
    assert output == 44
    output = Card("Joker", 54).card_to_number()
    assert output == 53
    output = Card("Hearts", 1).card_to_number()
    assert output == 27


def test_card_is_joker(card):
    output = card.is_joker()
    assert not output


def test_card_to_number_1_to_26(card):
    output = card.card_to_number_1_to_26()
    assert output == 5
