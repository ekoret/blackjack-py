"""Module for handling all game types"""

import abc
import sys


import pygame


from deck import Deck
from player import Dealer, Table, Player
from settings import Settings, BlackjackSettings
from player_menu import PlayerMenu
from game_menu import GameMenu
from menu import MainMenu

"""Abstract Game class"""


class Game(abc.ABC):
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()  # framerate
        self.font = pygame.font.SysFont(self.settings.font_name, 20)
        self.framerate = self.settings.framerate

        self.deck = Deck()
        self.player_count = 0
        self.current_player_turn = 1

        """Game states to control which screen is showing"""
        self.game_paused = False
        self.menu_state = "main"

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

        self.dealer = Dealer(self)
        self.table = Table(self)
        self.players = [self.dealer]

        self.bg_colour = self.settings.bg_colour
        self.amount_to_deal = self.settings.amount_to_deal
        self.moves = self.settings.moves

        self.last_update = pygame.time.get_ticks()

        self.game_menus = GameMenu(self)
        self.player_menu = PlayerMenu(self)

    """The game loop"""

    def run_game(self):
        self.add_player("John")
        self.add_player("Jack")
        self.add_player("Jane")

        self.deal_game()

        main_menu = MainMenu()

        if (len(self.players) == 2):
            self.players[1].x = self.settings.screen_width // 2
        elif (len(self.players) == 3):
            self.players[1].x = (self.settings.screen_width // 2) // 2
            self.players[2].x = self.settings.screen_width // 2
            + (self.settings.screen_width // 2) // 2
        elif (len(self.players) == 4):
            self.players[1].x = (self.settings.screen_width // 9)
            self.players[2].x = (self.settings.screen_width // 2)
            self.players[3].x = (self.settings.screen_width - 200)

        while (True):

            self.screen.fill(self.bg_colour)  # draw bg

            """Draw screens when applicable"""

            if (self.game_paused == True):
                if (self.menu_state == "main"):
                    main_menu.draw(self.screen)
            else:
                self.draw_dealer_sprite()
                self.draw_players()
                current_player = self.players[self.current_player_turn]
                self.player_menu.draw(current_player)
            """
            Event Loop
            Listen for keyboard presses and mouse clicks
            """
            self.run_event_loop()

            pygame.display.flip()  # update the screen
            self.clock.tick(self.framerate)  # set the framerate

    def run_event_loop(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN):
                """Handle pause"""
                if (event.key == pygame.K_SPACE):
                    print("Space pressed")
                    if (self.game_paused):
                        self.game_paused = False
                    else:
                        self.game_paused = True

    """TODO: needs to be refactored into Dealer"""

    def draw_dealer_sprite(self):
        current_time = pygame.time.get_ticks()

        if (current_time - self.last_update >= self.dealer.sprite.animation_cooldown):
            self.dealer.sprite.animations["standing"]["current_frame"] += 1
            self.last_update = current_time
            if (self.dealer.sprite.animations["standing"]["current_frame"] >= self.dealer.sprite.animations["standing"]["steps"]):
                self.dealer.sprite.animations["standing"]["current_frame"] = 0

        """Draw sprite, hand, and label"""
        self.dealer.sprite.draw(
            self.screen, self.dealer.sprite.animations["standing"]["current_frame"])
        # self.dealer.draw()

    def draw_players(self):
        for player in self.players:
            player.draw()

    def deal_game(self):
        for _ in range(self.amount_to_deal):
            for player in self.players[1:]:
                player.add_card(self.deck.deal_card())

        self.dealer.add_card(self.deck.deal_card())
