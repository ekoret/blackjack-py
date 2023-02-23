"""Module for creating buttons"""

import pygame


class GameButton:
    def __init__(self, x, y, width, height, text,
                 font_size=20,
                 font_name="Arial",
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

        self.font = pygame.font.SysFont(font_name, self.font_size)
        # self.rect = self.surface.get_rect()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x + (self.width / 2),
                            self.y + (self.height / 2))
        self.surface = self.font.render(self.text, True, self.bg_colour_hover)
        self.surface_rect = self.surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        if self.is_hovered(pygame.mouse.get_pos()):
            colour = self.bg_colour_hover
        else:
            colour = self.bg_colour

        pygame.draw.rect(screen, colour, self.rect)
        screen.blit(self.surface, self.surface_rect)

    def is_clicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
        # return self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)
