"""Classes for game settings"""

import abc


import pygame


"""Abstract Settings class"""


class Settings(abc.ABC):
    @property
    @abc.abstractmethod
    def screen_width(self):
        pass

    @property
    @abc.abstractmethod
    def screen_height(self):
        pass

    @property
    @abc.abstractmethod
    def bg_colour(self):
        pass

    @property
    @abc.abstractmethod
    def screen(self):
        pass


"""Blackjack settings"""


class BlackjackSettings(Settings):

    def __init__(self):
        self.game_name = "Blackjack"
        self._screen_width = 1200
        self._screen_height = 800
        self._bg_colour = (50, 50, 50)

        """Blackjack specific attributes"""
        self.amount_to_deal = 2
        self.moves = ["Hit", "Pass", "Split", "Double", "Fold"]
        self._screen = pygame.display.set_mode(
            (self._screen_width, self._screen_height))

    """Getter for screen width"""
    @property
    def screen_width(self):
        return self._screen_width

    """Getter for screen height"""
    @property
    def screen_height(self):
        return self._screen_height

    """Getter for background colour"""
    @property
    def bg_colour(self):
        return self._bg_colour

    """Getter for screen"""
    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value):
        self._screen = value
