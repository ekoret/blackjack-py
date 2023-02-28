"""Module for handling all game types"""

import abc
import sys


import pygame


from deck import Deck
from player import Dealer, Table, Player
from settings import Settings, BlackjackSettings
from player_menu import PlayerMenu
from menu import MainMenu, GameEndMenu


class Game(abc.ABC):
    """Abstract Game class"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()  # framerate
        self.font = pygame.font.SysFont(self.settings.font_name, 20)
        self.framerate = self.settings.framerate

        """Game players, stats, assets"""
        self.deck = Deck()
        self.players = []
        self.player_count = 0
        self.current_player_turn = 1

        """Game states to control which screen is showing"""
        self.game_paused = False
        self.menu_state = "main"
        self.game_over = False

    def add_player(self, name):
        """Increase the player count and add them to player list, then return player"""
        self.player_count += 1
        player = Player(self, f"{self.player_count} - {name}")
        self.players.append(player)
        return player

    @abc.abstractmethod
    def run_game(self):
        """Initialize game then run game loop"""
        pass

    @abc.abstractmethod
    def deal_game(self):
        """Deal cards to players"""
        pass


class BlackJack(Game):
    """Game subclass Blackjack"""

    def __init__(self):
        super().__init__()

        self.settings = BlackjackSettings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.dealer = Dealer(self)
        self.table = Table(self)
        self.players = [self.dealer]

        self.bg_colour = self.settings.bg_colour
        self.amount_to_deal = self.settings.amount_to_deal
        self.moves = self.settings.moves

        self.last_update = pygame.time.get_ticks()

        """Menus"""
        self.player_menu = PlayerMenu(self)
        self.main_menu = MainMenu(self)
        self.game_end_menu = GameEndMenu(self)

    def run_game(self):
        """Initialize game then run main game loop."""

        self.add_player("John")
        # self.add_player("Jack")
        # self.add_player("Jane")

        self.deal_game()

        # pylint: disable=pointless-string-statement
        """Seating players depending on amount of players"""
        if len(self.players) == 2:
            self.players[1].x = self.settings.screen_width // 2
        elif len(self.players) == 3:
            self.players[1].x = (self.settings.screen_width // 2) // 2
            self.players[2].x = (
                self.settings.screen_width // 2 + (self.settings.screen_width // 2) // 2
            )
        elif len(self.players) == 4:
            self.players[1].x = self.settings.screen_width // 9
            self.players[2].x = self.settings.screen_width // 2
            self.players[3].x = self.settings.screen_width - 200

        while True:
            self.screen.fill(self.bg_colour)  # Draw background

            """Draw screens when applicable"""
            if self.game_paused is True:
                if self.menu_state == "main":
                    self.main_menu.draw(self.screen)

            else:
                if self.game_over is True:
                    # show who wins or loses
                    # buttons to reset or quit game
                    self.game_end_menu.draw(self.screen)

                self.draw_dealer_sprite()
                self.draw_players()

                """Dealers turn, end game"""
                if self.current_player_turn == 0:
                    self.dealer.play()
                    self.game_over = True

                if self.current_player_turn > len(self.players) - 1:
                    self.current_player_turn = 0
                current_player = self.players[self.current_player_turn]

                """Do not show player menu if player is dealer"""
                if self.current_player_turn != 0:
                    self.player_menu.draw(current_player)

            """
            Event Loop
            Listen for keyboard presses and mouse clicks
            """
            self.run_event_loop(self, current_player)

            pygame.display.flip()  # update the screen
            self.clock.tick(self.framerate)  # set the framerate

    def run_event_loop(self, game, current_player):
        """Event loop for listening to button clicks, keypresses, mouse movements"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    """Handle Pause"""  # pylint: disable=pointless-string-statement
                    print("Space pressed")
                    if self.game_paused:
                        self.game_paused = False
                    else:
                        self.game_paused = True

            for button in self.player_menu.buttons:
                button.handle_events(event, game, current_player)

            for button in self.game_end_menu.buttons:
                button.handle_events(event, game, current_player)

    def draw_dealer_sprite(self):
        """
        Draws and animates the dealers sprite.

        TODO
        -
        Needs to be refactored into Dealer.
        """

        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >= self.dealer.sprite.animation_cooldown:
            current_frame = self.dealer.sprite.animations["standing"]["current_frame"]
            current_frame += 1

            self.last_update = current_time
            total_animation_steps = self.dealer.sprite.animations["standing"]["steps"]

            if current_frame >= total_animation_steps:
                current_frame = 0

        """TODO: refactor this out of draw_dealer_sprite"""  # pylint: disable=pointless-string-statement
        self.dealer.sprite.draw(
            self.screen, self.dealer.sprite.animations["standing"]["current_frame"]
        )
        # self.dealer.draw()

    def draw_players(self):
        """Loop through list of players and display on screen"""
        for player in self.players:
            player.draw()

    def deal_game(self):
        for _ in range(self.amount_to_deal):
            for player in self.players[1:]:
                player.add_card(self.deck.deal_card())

        self.dealer.add_card(self.deck.deal_card())
