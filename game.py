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
        self.players.append(player)
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
        super().__init__()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        """Pygame init"""
        self.bg_colour = self.settings.bg_colour

        """Self init"""
        self.amount_to_deal = self.settings.amount_to_deal
        self.moves = self.settings.moves

    """The game loop"""

    def run_game(self):
        self.add_player("John")
        self.add_player("Jack")
        self.add_player("Jane")
        self.deal_game()

        while (True):
            """Event Loop"""
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()

            """Pygame function and method calls"""
            self.screen.fill(self.bg_colour)  # bg

            """Draw players and dealer"""
            self.dealer.draw()
            self.draw_players()
            self.table.draw()
            self.table.draw_remaining_cards()

            pygame.display.flip()
            self.clock.tick(self.framerate)  # set the framerate

    def draw_players(self):
        total_players = len(self.players)
        if (total_players == 2):
            """Draw player in center"""
            player1 = self.players[1]
            player1.draw(self.settings.screen_width // 2, (255, 0, 0))

        elif (total_players == 3):
            player1 = self.players[1]
            player2 = self.players[2]
            player1.draw((self.settings.screen_width // 2) // 2, (255, 0, 0))
            player2.draw((self.settings.screen_width // 2) +
                         (self.settings.screen_width // 2) // 2, (0, 0, 255))

        elif (total_players == 4):
            player1 = self.players[1]
            player1.draw(self.settings.screen_width // 9, (255, 0, 0))
            player2 = self.players[2]
            player2.draw(self.settings.screen_width // 2, (0, 0, 255))
            player3 = self.players[3]
            player3.draw(self.settings.screen_width - 200, (0, 255, 0))

    """Method for dealing the Blackjack game"""

    def deal_game(self):
        # adds cards to players first then table
        for _ in range(self.amount_to_deal):
            for player in self.players:
                player.add_card(self.deck.deal_card())

        self.table.add_card(self.deck.deal_card())
