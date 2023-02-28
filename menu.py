"""Module for handling menus"""

from game_button import GameButton


class Menu:
    """Base menu. Has access to the game."""

    def __init__(self, game, name=""):
        self.game = game
        self.name = name


class MainMenu(Menu):
    """Main menu is used for the pause menu for displaying quick actions."""

    def __init__(self, game):
        super().__init__(game)
        self.x = 500
        self.name = "Main Menu"

        # fmt: off
        self.resume_button = GameButton(
            self.x, 100, 200, 100, "Resume", 20, "Arial", (255, 255, 255), (0, 0, 0), (30, 30, 30))
        self.reset_button = GameButton(
            self.x, 100 + (100 * 2 + 10), 200, 100, "Reset", 20, "Arial", (255, 255, 255), (170, 50, 50), (100, 20, 20))
        self.quit_button = GameButton(
            self.x, 100 + (100 * 3 + 10), 200, 100, "Quit", 20, "Arial", (255, 255, 255), (0, 0, 0), (30, 30, 30))

    def draw(self, screen):
        """Display the resume, reset, and quit buttons."""

        self.resume_button.draw(screen)
        self.reset_button.draw(screen)
        self.quit_button.draw(screen)


class GameEndMenu(Menu):
    """Menu for when the game ends"""

    def __init__(self, game):
        super().__init__(game)

        self.name = "Game End"

        self.buttons = [GameButton(100, 100, 200, 100, "RESET")]

    def draw(self, screen):
        """Draw buttons for the game end menu."""
        for button in self.buttons:
            button.draw(screen)
