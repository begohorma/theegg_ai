class Card:

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    def get_suit(self):
        return self._suit

    def get_rank(self):
        return self._rank

    def __str__(self):
        # devolver la carta como un string formado por el valor y la inicial del palo
        return str(self._rank) + self._suit[0]

    def show(self):
        print("{0} of {1}".format(self.get_rank(), self.get_suit()))

    def card_to_number(self):
        if self._suit == "Clubs":
            return self._rank
        if self._suit == "Diamonds":
            return self._rank + 13
        if self._suit == "Hearts":
            return self._rank + 26
        if self._suit == "Spades":
            return self._rank + 39
        else:
            return 53

    def is_joker(self):
        return self._suit == "Joker"

    def card_to_number_1_to_26(self):
        if self._suit == "Clubs" or self._suit == "Hearts":
            return self._rank
        if self._suit == "Diamonds" or self._suit == "Spades":
            return self._rank + 13
