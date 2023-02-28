"""Classes for game settings"""

import abc


class Settings(abc.ABC):
    """Settings class for general settings"""

    def __init__(self):
        self.font_name = "Arial"
        self.framerate = 30


class BlackjackSettings(Settings):
    """Blackjack specific settings. Derives from Settings"""

    def __init__(self):
        super().__init__()

        self.game_name = "Blackjack"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (50, 50, 50)

        self.amount_to_deal = 2
        self.moves = ["Hit", "Stay"]
