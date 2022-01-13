class Battle:
    turn = 0  # comienza el pokemon con el turno 0

    def __init__(self, pokemon_1, pokemon_2):
        self._pokemon_1 = self.get_first_pokemon(pokemon_1, pokemon_2)
        self._pokemon_2 = self.get_second_pokemon(pokemon_1, pokemon_2)

    @staticmethod
    def get_first_pokemon(pk1, pk2):
        return pk1 if pk1.get_turn() == 0 else pk2

    @staticmethod
    def get_second_pokemon(pk1, pk2):
        return pk1 if pk1.get_turn() == 1 else pk2

    def battle(self):
        print("¡¡¡ Batalla pokemon entre {0} y {1} !!!".format(self._pokemon_1.get_name(), self._pokemon_2.get_name()))

        while self._pokemon_1.get_life() > 0 and self._pokemon_2.get_life() > 0:
            if self.turn == 0:
                print(self._pokemon_1.attack())
                self._pokemon_2.set_life(self._pokemon_2.get_life() - self._pokemon_1.get_attack())
                print(self._pokemon_2.life())
                self.turn = 1
            elif self.turn == 1:
                print(self._pokemon_2.attack())
                self._pokemon_1.set_life(self._pokemon_1.get_life() - self._pokemon_2.get_attack())
                print(self._pokemon_1.life())
                self.turn = 0

        if self._pokemon_1.get_life() <= 0:
            print(self._pokemon_2.win())
        else:
            print(self._pokemon_1.win())
