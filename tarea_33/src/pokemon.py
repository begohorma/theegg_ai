class Pokemon:

    def __init__(self, name, attack, turn):
        self._name = name
        self._attack = attack
        self._turn = turn
        self._life = 100

    def get_name(self):
        return self._name

    def get_attack(self):
        return self._attack

    def get_life(self):
        return self._life

    def get_turn(self):
        return self._turn

    def set_life(self, value):
        self._life = value

    def attack(self):
        return "{0} realiza un ataque de potencia {1}".format(self.get_name(), self.get_attack())

    def win(self):
        return "{0} ha ganado la batalla".format(self.get_name())

    def life(self):
        return "La vida de {0} es {1}".format(self.get_name(), self.get_life())
