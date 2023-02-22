import pygame


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

    def draw(self):
        """Single player + dealer"""
        if (len(self.game.players) == 2):
            """Draw player in center"""
            square = Square(1200 // 2,
                            800 - 100, 50, (255, 0, 0), self.name, 20)
            square.draw(self.screen)

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

    """The dealer always sits at the same place"""

    def draw(self):
        self.draw_rect()
        self.draw_label("Dealer")

    def draw_rect(self):
        pygame.draw.rect(self.screen, (200, 50, 50),
                         pygame.Rect(self.game.settings.screen_width / 2, 50, 60, 60))

    def draw_label(self, label):
        text = self.game.font.render(label,
                                     True, (255, 255, 255))
        x = self.game.settings.screen_width / 2
        y = 80
        self.game.screen.blit(text, (x, y))


class Table(Player):
    def __init__(self, game):
        super().__init__(game)
        self.name = "Table"
        self.graveyard = []

    def __str__(self):
        return f"Table({self.name})"
