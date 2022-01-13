import random
from aux_functions import get_correct_attack_value
from pokemon import Pokemon
from battle import Battle


def main():
    # obtener los datos de los pokemons
    pokemon_1_name = input("Indica el nombre del primer pokemon: ")
    pokemon_1_attack = get_correct_attack_value("Indica la potencia de ataque del primer pokemon. Valor de 1 a 100. :")
    pokemon_2_name = input("Indica el nombre del segundo pokemon :")
    pokemon_2_attack = get_correct_attack_value("Indica la potencia de ataque del segundo pokemon. Valor de 1 a 100. :")

    # generar aleatoriamente un valor 0 o 1
    r_turn = random.randint(0, 1)

    # asignar al primer pokemon el valor de turno aleatorio y al segundo el contrario
    pokemon_1 = Pokemon(pokemon_1_name, pokemon_1_attack, r_turn)
    pokemon_2 = Pokemon(pokemon_2_name, pokemon_2_attack, int(not r_turn))
    b = Battle(pokemon_1, pokemon_2)
    b.battle()


if __name__ == '__main__':
    main()
