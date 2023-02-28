"""Module is for creating game object GameText."""


import pygame


class GameText:
    """Creates game object GameText for displaying."""

    def __init__(
        self,
        label_text,
        font_size=20,
        font_name="Arial",
        text_colour=(255, 255, 255),
        bg_colour=(0, 0, 0),
    ):
        self.label_text = label_text
        self.font_size = font_size
        self.font = pygame.font.SysFont(font_name, self.font_size)
        self.label = self.font.render(self.label_text, True, text_colour, bg_colour)

    def draw(self, screen, x, y):
        """Display text on main game screen"""
        screen.blit(self.label, (x, y))
