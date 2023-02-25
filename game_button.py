"""Module for creating buttons"""

import pygame


class GameButton:
    def __init__(self, x, y, width, height, text,
                 font_size=20,
                 font_name="Arial",
                 text_colour=(255, 255, 255),
                 bg_colour=(150, 150, 150),
                 bg_colour_hover=(170, 10, 200)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.bg_colour = bg_colour
        self.bg_colour_hover = bg_colour_hover
        self.text_colour = text_colour

        self.clicked = False

        """Define font"""
        self.font = pygame.font.SysFont(font_name, self.font_size)

        """Create rect, set dimensions, set coordinates from center"""
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x + (self.width / 2),
                            self.y + (self.height / 2))

        """Create text, set styles, set coordinate from center of rect"""
        self.surface = self.font.render(self.text, True, self.text_colour)
        self.surface_rect = self.surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        color = self.bg_colour

        """Check if mouse is hovering over button then if button clicked"""
        if (self.rect.collidepoint(mouse_pos)):
            color = self.bg_colour_hover
            if (pygame.mouse.get_pressed()[0] == 1 and self.clicked == False):
                self.clicked = True
                print('clicked')

        if (pygame.mouse.get_pressed()[0] == 0):
            self.clicked = False

        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.surface, self.surface_rect)
