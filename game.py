"""Module for handling all game types"""

import abc
import sys


import pygame


from deck import Deck
from player import Dealer, Table, Player
from settings import Settings, BlackjackSettings

"""Abstract Game class"""


class Game(abc.ABC):
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()  # framerate
        self.font = pygame.font.SysFont(self.settings.font_name, 20)
        self.framerate = self.settings.framerate

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
        super().__init__()

        self.settings = BlackjackSettings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.bg_colour = self.settings.bg_colour
        self.amount_to_deal = self.settings.amount_to_deal
        self.moves = self.settings.moves

        self.last_update = pygame.time.get_ticks()

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
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.bg_colour)  # draw bg

            """Draw players and dealer"""
            self.draw_players()
            self.draw_dealer()
            self.table.draw_remaining_cards()

            pygame.display.flip()  # update the screen
            self.clock.tick(self.framerate)  # set the framerate

    def draw_dealer(self):
        """Update sprite animation"""
        current_time = pygame.time.get_ticks()

        if (current_time - self.last_update >= self.dealer.sprite.animation_cooldown):
            self.dealer.sprite.animations["standing"]["current_frame"] += 1
            self.last_update = current_time
            if (self.dealer.sprite.animations["standing"]["current_frame"] >= self.dealer.sprite.animations["standing"]["steps"]):
                self.dealer.sprite.animations["standing"]["current_frame"] = 0

        """Draw sprite, hand, and label"""
        self.dealer.sprite.draw(
            self.screen, self.dealer.sprite.animations["standing"]["current_frame"])
        self.dealer.draw()

    """
    TODO: needs to be refactored
        - put players in positions depending on amount of players
    """

    def draw_players(self):

        total_players = len(self.players)
        if (total_players == 2):
            """Draw player in center"""
            self.players[1].draw(self.settings.screen_width // 2)

        elif (total_players == 3):
            self.players[1].draw((self.settings.screen_width // 2) // 2)
            self.players[2].draw((self.settings.screen_width // 2) +
                                 (self.settings.screen_width // 2) // 2)

        elif (total_players == 4):
            self.players[1].draw(self.settings.screen_width // 9)
            self.players[2].draw(self.settings.screen_width // 2)
            self.players[3].draw(self.settings.screen_width - 200)

    """Method for dealing the Blackjack game"""

    def deal_game(self):
        for _ in range(self.amount_to_deal):
            for player in self.players[1:]:
                player.add_card(self.deck.deal_card())

        self.dealer.add_card(self.deck.deal_card())
