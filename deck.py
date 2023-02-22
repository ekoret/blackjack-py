import random
from card import Card


class Deck:
    def __init__(self):
        self.max_cards = (52,)
        self.suits = ("S", "C", "D", "H")
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
        self.cards = self.create()

    """Gets called on Deck instantiation to get a full shuffled deck"""

    def create(self):
        deck = []
        for value in self.values:
            for suit in self.suits:
                card = Card(value, suit)
                deck.append(card)
        self.shuffle(deck)
        return deck

    """Method for dealing a single card from the top of the deck"""

    def deal_card(self):
        card = self.cards.pop()
        return card

    """Method for getting remaining cards as values in a list"""

    def get_remaining_cards(self):
        cards = [str(card) for card in self.cards]
        return cards

    """Helper method for shuffling the deck"""

    def shuffle(self, list):
        random.shuffle(list)
