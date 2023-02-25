"""Classes for game settings"""

import abc


"""Abstract Settings class"""


class Settings(abc.ABC):
    def __init__(self):
        self.font_name = "Arial"
        self.framerate = 30


"""Blackjack settings"""


class BlackjackSettings(Settings):

    def __init__(self):
        self.game_name = "Blackjack"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (50, 50, 50)

        """Blackjack specific attributes"""
        self.amount_to_deal = 2
        self.moves = ["Hit", "Stay"]
