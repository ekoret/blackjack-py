

from square import Square


class Player:
    def __init__(self, game, name=""):
        """Pygame init"""
        self.game = game
        self.screen = game.screen

        """Self init"""
        self.name = name
        self.hand = []
        self.cards_played = []

    def __str__(self):
        return f"Player({self.name})"

    def draw(self, x, colour):
        y = 800 - 125
        size = 75
        font_size = 20

        player = Square(x,
                        y, size, colour, self.name, font_size)
        player.draw(self.screen)

    """Adds a single card to players hand"""

    def add_card(self, card):
        self.hand.append(card)

    """Plays a card from the players hand
    TODO: needs to be refactored to take in an index instead
    """

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.cards_played.append(card)
            return card
        else:
            raise ValueError(f"Card not found in {self.name}'s hand")

    """Returns string format of cards"""

    def get_hand(self, list=False):
        if list:
            return [str(card) for card in self.hand]

        return " - ".join(str(card) for card in self.hand)


class Dealer(Player):
    def __init__(self, game):
        super().__init__(game)
        self.name = "Dealer"

    def __str__(self):
        return f"Dealer({self.name})"

    def draw(self):
        x = self.game.settings.screen_width // 2
        y = 125
        size = 75
        font_size = 20

        dealer = Square(x,
                        y, size, (200, 200, 0), self.name, font_size)
        cards = Square(x,
                       y + 200, size, (200, 200, 0), str(self.get_hand()), font_size)
        dealer.draw(self.screen)
        cards.draw(self.screen)


class Table(Player):
    def __init__(self, game):
        super().__init__(game)
        self.name = "Table"
        self.graveyard = []

    def __str__(self):
        return f"Table({self.name})"
