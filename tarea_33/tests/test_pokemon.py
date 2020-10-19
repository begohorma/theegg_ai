import pytest
from pokemon import Pokemon


@pytest.fixture()
def pokemon():
    pk = Pokemon("Pikachu", 55, 0)
    return pk


def test_get_pokemon_name(pokemon):
    output = pokemon.get_name()
    assert output == "Pikachu"


def test_get_pokemon_attack(pokemon):
    output = pokemon.get_attack()
    assert output == 55


def test_get_pokemon_turn(pokemon):
    output = pokemon.get_turn()
    assert output == 0


def test_pokemon_win(pokemon):
    output = pokemon.win()
    assert output == "¡¡ Pikachu ha ganado la batalla!!"
