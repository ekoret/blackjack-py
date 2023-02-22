import abc
import sys


import pygame


from deck import Deck
from player import Dealer, Table, Player
from settings import BlackjackSettings

"""Abstract Game class"""


class Game(abc.ABC):
    def __init__(self):
        """Pygame init"""
        self.pygame_instance = pygame
        self.clock = pygame.time.Clock()  # framerate
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 20)
        self.framerate = 30

        """Self init"""
        self.deck = Deck()
        self.dealer = Dealer(self)
        self.table = Table(self)
        self.players = [self.dealer]
        self.player_count = 0

    """Method for adding a player to the game"""

    def add_player(self, name):
        self.player_count += 1
        player = Player(self, f"{self.player_count} - {name}")
        return player

    """Abstract method for running game loop"""
    @abc.abstractmethod
    def run_game(self):
        pass

    """Abstract method for dealing a game"""
    @abc.abstractmethod
    def deal_game(self):
        pass


"""Game subclass Blackjack"""


class BlackJack(Game):
    def __init__(self):
        self.settings = BlackjackSettings()
        self.screen = self.settings.screen
        super().__init__()
        """Pygame init"""
        self.bg_colour = self.settings.bg_colour

        """Self init"""
        self.amount_to_deal = self.settings.amount_to_deal
        self.moves = self.settings.moves

    """The game loop"""

    def run_game(self):

        john = self.add_player("John")

        while (True):
            """Event Loop"""
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()

            """Pygame function and method calls"""
            self.screen.fill(self.settings.bg_colour)  # bg

            self.dealer.draw()
            john.draw()

            pygame.display.flip()
            self.clock.tick(self.framerate)  # set the framerate

    """Method for dealing the Blackjack game"""

    def deal_game(self):

        # adds cards to players first then table
        for _ in range(self._deal):
            for player in self.player_list:
                player.add_card(self.deck.deal_card())

        self.table.add_card(self.deck.deal_card())
