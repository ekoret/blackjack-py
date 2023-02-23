

from square import Square


class Player:
    def __init__(self, game, name=""):
        """Pygame init"""
        self.game = game

        """Self init"""
        self.name = name
        self.hand = []
        self.cards_played = []

    def __str__(self):
        return f"Player({self.name})"

    def draw(self, x, colour):
        y = self.game.settings.screen_height - 200
        size = 75
        font_size = 20

        player = Square(x,
                        y, size, colour, self.name, font_size)
        cards = Square(
            x, y + 25, 75, self.game.bg_colour, self.get_hand(), 20)
        cards.draw(self.game.screen)
        player.draw(self.game.screen)

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
                       y + 25, size, self.game.bg_colour, self.get_hand(), font_size)
        cards.draw(self.game.screen)
        dealer.draw(self.game.screen)


class Table(Player):
    def __init__(self, game):
        super().__init__(game)
        self.name = "Table"
        self.graveyard = []

    def __str__(self):
        return f"Table({self.name})"

    def draw(self):
        x = self.game.settings.screen_width // 2
        y = self.game.settings.screen_height // 2

        table = Square(x, y, 100, (77, 25, 0), self.get_hand(), 20)
        table.draw(self.game.screen)

    def draw_remaining_cards(self):
        x = 500
        y = 200

        remaining_cards = self.game.deck.get_remaining_cards()
        remaining_deck_total = len(remaining_cards)

        """TODO: needs to be refactored"""
        first_half = '  '.join(remaining_cards[:remaining_deck_total // 2])
        second_half = '  '.join(remaining_cards[remaining_deck_total // 2:])
        remaining_cards_first = Square(
            x, y, 100, self.game.bg_colour, first_half, 20)
        remaining_cards_second = Square(
            x, y + 20, 100, self.game.bg_colour, second_half, 20)
        remaining_cards_first.draw(self.game.screen)
        remaining_cards_second.draw(self.game.screen)
