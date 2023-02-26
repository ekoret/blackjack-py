from game_button import GameButton


class Menu:
    def __init__(self, name=""):
        self.name = name


class MainMenu(Menu):
    def __init__(self):
        super().__init__()
        self.x = 500
        self.name = "Main Menu"
        self.resume_button = GameButton(
            self.x, 100, 200, 100, "Resume", 20, "Arial", (255, 255, 255), (0, 0, 0), (30, 30, 30))
        self.reset_button = GameButton(
            self.x, 100 + (100 * 2 + 10), 200, 100, "Reset", 20, "Arial", (255, 255, 255), (170, 50, 50), (100, 20, 20))
        self.quit_button = GameButton(
            self.x, 100 + (100 * 3 + 10), 200, 100, "Quit", 20, "Arial", (255, 255, 255), (0, 0, 0), (30, 30, 30))

    def draw(self, screen):

        self.resume_button.draw(screen)
        self.reset_button.draw(screen)
        self.quit_button.draw(screen)
