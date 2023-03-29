import random

from icecream import ic

from card import Card


class Deck:
    def __init__(self, game):
        self.game = game
        self.suits = ("spades", "clubs", "diamonds", "hearts")
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")

        self.init_cards()

    def init_cards(self):
        cards = []
        for suit in self.suits:
            for value in self.values:
                cards.append(Card(value, suit))
        self._shuffle(cards)
        self.cards = cards

    def _shuffle(self, cards):
        random.shuffle(cards)

    def get_top_card(self):
        card = self.cards.pop()
        return card
