
from game_text import GameText


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

    def draw(self, x):
        y = self.game.settings.screen_height - 200

        player_label = GameText(self.name)
        cards_label = GameText(self.get_hand())

        cards_label.draw(self.game.screen, x, y + 20)
        player_label.draw(self.game.screen, x, y)

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

        dealer_label = GameText("Dealer")
        player_cards_label = GameText(self.get_hand())

        player_cards_label.draw(self.game.screen, x, y + 20)
        dealer_label.draw(self.game.screen, x, y)


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

        table_label = GameText("Table")
        table_cards_label = GameText(self.get_hand())
        table_label.draw(self.game.screen, x, y)
        table_cards_label.draw(self.game.screen, x, y + 20)

    def draw_remaining_cards(self):
        x = 300
        y = 200

        remaining_cards = self.game.deck.get_remaining_cards()
        remaining_deck_total = len(remaining_cards)

        """TODO: needs to be refactored"""
        first_half = '  '.join(remaining_cards[:remaining_deck_total // 2])
        second_half = '  '.join(remaining_cards[remaining_deck_total // 2:])

        remaining_cards_first = GameText(first_half)
        remaining_cards_second = GameText(second_half)

        remaining_cards_first.draw(self.game.screen, x, y)
        remaining_cards_second.draw(self.game.screen, x, y + 20)
