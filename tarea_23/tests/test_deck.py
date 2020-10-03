import pytest
from deck import Deck

@pytest.fixture()
def deck():
    deck = Deck("")
    return deck


def test_deck_with_no_key(deck):
    output = str(deck)
    assert output == "1C2C3C4C5C6C7C8C9C10C11C12C13C1D2D3D4D5D6D7D8D9D10D11D12D13D1H2H3H4H5H6H7H8H9H10H11H12H13H1S2S3S4S5S6S7S8S9S10S11S12S13S53J54J"


def test_find_card_position(deck):
    output = deck.find_card_position("Joker", 53)
    assert output == 52
    output = deck.find_card_position("Hearts", 3)
    assert output == 28


def test_move_card_one_down(deck):
    position1 = deck.find_card_position("Hearts", 3)
    deck.move_card_one_position_down(position1)
    position2 = deck.find_card_position("Hearts", 3)
    assert position2 == position1 + 1
    assert position2 == 29


def test_move_last_card_one_down(deck):
    cards = deck.get_cards()
    last_card = cards[53]
    deck.move_card_one_position_down(53)
    position = deck.find_card_position(last_card.get_suit(), last_card.get_rank())
    assert position == 0


def test_move_card_two_down(deck):
    position1 = deck.find_card_position("Hearts", 3)
    deck.move_card_two_position_down(position1)
    position2 = deck.find_card_position("Hearts", 3)
    assert position2 == position1 + 2


def test_move_last_card_two_down(deck):
    cards = deck.get_cards()
    last_card = cards[53]
    deck.move_card_two_position_down(53)
    position = deck.find_card_position(last_card.get_suit(), last_card.get_rank())
    assert position == 2


def test_move_penultimate_card_two_down(deck):
    cards = deck.get_cards()
    penultimate_card = cards[52]
    deck.move_card_two_position_down(52)
    position = deck.find_card_position(penultimate_card.get_suit(), penultimate_card.get_rank())
    assert position == 1


def test_find_first_joker_position(deck):
    position = deck.find_card_position_by_rank(53)
    assert position == 52


def test_triple_cut(deck):
    cards = deck.get_cards()
    ja_position = deck.find_card_position_by_rank(53)
    jb_position = deck.find_card_position_by_rank(54)
    if ja_position < jb_position:
        first_position = ja_position
        second_position = jb_position
    else:
        first_position = jb_position
        second_position = ja_position

    part_1 = cards[:first_position]
    part_2 = cards[first_position:second_position + 1]
    part_3 = cards[second_position + 1:]

    deck.triple_cut(first_position, second_position)
    new_cards = deck.get_cards()

    assert new_cards == part_3 + part_2 + part_1


def test_count_cut(deck):

    cards = deck.get_cards()
    position = cards[53].card_to_number()

    part_1 = cards[:position]
    part_2 = cards[position:-1]
    last_card = cards[53]

    deck.count_cut(position)
    new_cards = deck.get_cards()

    assert new_cards == part_2 + part_1 + [last_card]
