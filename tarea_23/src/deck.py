from card import Card


class Deck:
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, key_numbers):
        self._cards = []
        self.build()
        self._key_numbers = key_numbers

    def build(self):
        # crear baraja con el orden por defecto
        for s in Deck.SUITS:
            for r in range(1, 14):
                self._cards.append(Card(s, r))
        # añadir comodines
        self._cards.append(Card("Joker", 53))
        self._cards.append(Card("Joker", 54))

    def get_cards(self):
        return self._cards

    def __str__(self):
        return "".join(str(card) for card in self._cards)

    def apply_key(self, key_numbers):
        self._key_numbers = key_numbers
        for n in range(0, len(self._key_numbers)):
            self.apply_key_number(self._key_numbers[n])

    def apply_key_number(self, key_num):
        # mover JokerA
        ja_position = self.find_card_position_by_rank(53)
        self.move_card_one_position_down(ja_position)
        # mover JokerB
        jb_position = self.find_card_position_by_rank(54)
        self.move_card_two_position_down(jb_position)
        # triple corte
        ja_position = self.find_card_position_by_rank(53)
        jb_position = self.find_card_position_by_rank(54)
        if ja_position < jb_position:
            self.triple_cut(ja_position, jb_position)
        else:
            self.triple_cut(jb_position, ja_position)
        # corte segun posición valor última carta
        self.count_cut(self.get_cards()[53].card_to_number())
        # corte segun posición valor letra de la clave
        self.count_cut(key_num)

    def find_card_position(self, suit, rank):
        for i in range(len(self._cards)):
            if self._cards[i].get_suit() == suit and self._cards[i].get_rank() == rank:
                return i

    def find_card_position_by_rank(self, rank):
        for i in range(len(self._cards)):
            if self._cards[i].get_rank() == rank:
                return i

    def move_card_one_position_down(self, position):
        card_to_move = self._cards[position]
        if position == 53:
            # si es la ultima posición intercambiar con la primera carta
            # en la posición actual asignar la primera carta
            self._cards[position] = self._cards[0]
            # en la primera  posición asignar la carta a mover
            self._cards[0] = card_to_move
        else:
            # en la posición actual asignar la carta posterior
            self._cards[position] = self._cards[position + 1]
            # en la siguiente posición asignar la carta a mover
            self._cards[position + 1] = card_to_move

    def move_card_two_position_down(self, position):
        card_to_move = self._cards[position]
        # si es la última carta ponerla debajo de la segunda carta
        if position == 53:
            self._cards.insert(2, card_to_move)
            self._cards.pop(position + 1)
        # si es la penúlitma carta ponerla debajo de la primera
        if position == 52:
            self._cards.insert(1, card_to_move)
            self._cards.pop(position + 1)
        else:
            self._cards.insert(position + 3, card_to_move)
            self._cards.pop(position)

    def triple_cut(self, first_position, second_position):
        part_1 = self._cards[:first_position]
        part_2 = self._cards[first_position:second_position + 1]
        part_3 = self._cards[second_position + 1:]

        self._cards = part_3 + part_2 + part_1

    def count_cut(self, position):
        part_1 = self._cards[:position]
        part_2 = self._cards[position:-1]
        part_3 = [self._cards[53]]

        self._cards = part_2 + part_1 + part_3
