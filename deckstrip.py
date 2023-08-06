import random


class Card:
    RANKS = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
             'K': 13}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def __str__(self):
        return f"{self._value} of {self._suit}"

    def __repr__(self):
        return f'{self.__class__.__name__}{self._suit, self._value}'



    @property
    def value(self):
        """ Used for extraction of card value"""
        return self._value

    @property
    def suit(self):
        """ Used for extraction of card suit"""
        return self._suit

    @classmethod
    def _convert(cls, a):
        """Helps in checking value of card.Binds its str image to appropriate value"""
        return Card.RANKS[a]

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self._value == other._value and self._suit == other._suit

    def __lt__(self, other):
        return self._suit == other._suit and self._convert(self._value) < self._convert(other._value)

    def __sub__(self, other):
        if not isinstance(other, Card) and self._suit != other._suit:
            raise Exception('Substracts only objects of Card class with same suits')
        return self._convert(self._value) - other._convert(other._value)


class Deck:
    SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
    VALUES = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self):
        self._cards = []
        for suit in self.SUITS:
            for value in self.VALUES:
                card = Card(suit, value)
                self._cards.append(card)

    def shuffle(self):
        """Shuffle deck"""
        random.shuffle(self._cards)

    def deal(self):
        """Deal the card"""
        if self._cards:
            return self._cards.pop()
        else:
            return None

    def __repr__(self):
        return f"Deck of {len(self._cards)} cards"


