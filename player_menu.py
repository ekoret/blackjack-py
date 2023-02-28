"""Module for handling the Player Menu for making moves"""

import pygame

from game_button import GameButton


class PlayerMenu:
    """Displays the player menu for choosing an action."""

    def __init__(self, game):
        self.game = game

        self.height = 110
        self.width = 250

        self.x_offset = 80
        self.y_offset = 110

        self.bg_colour = (0, 0, 0)
        self.text_colour = (255, 255, 255)

        self.buttons = [
            GameButton(
                100,
                100,
                self.width - 10,
                (self.height // 2) - 10,
                "HIT",
                20,
                "Arial",
                (255, 255, 255),
                (15, 15, 15),
                (25, 25, 25),
            ),
            GameButton(
                100,
                150,
                self.width - 10,
                (self.height // 2 - 10),
                "STAY",
                20,
                "Arial",
                (255, 255, 255),
                (15, 15, 15),
                (25, 25, 25),
            ),
        ]

    def draw(self, player):
        """Draws and displays the menu and buttons"""

        menu_rect = pygame.Rect(
            player.x - self.x_offset, player.y - self.y_offset, self.width, self.height
        )

        """Draw menu container"""  # pylint: disable=pointless-string-statement
        pygame.draw.rect(self.game.screen, (180, 70, 70), menu_rect, 0, 4)

        for i, button in enumerate(self.buttons):
            """Draw menu buttons and change their positions"""  # pylint: disable=pointless-string-statement

            x = menu_rect.centerx
            y = menu_rect.y + 27 + (i * self.height // 2)
            button.rect.center = (x, y)

            """Change position of font to new button position"""  # pylint: disable=pointless-string-statement
            button.surface_rect = button.surface.get_rect(center=button.rect.center)

            button.draw(self.game.screen)
