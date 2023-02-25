import pygame

from game_button import GameButton


class GameMenu:
    def __init__(self, game):
        self.game = game

    def draw_start_menu(self):
        self.draw_menu_background()

    def draw_menu_background(self):
        rect = pygame.Rect(100, 200, 600, 300)
        rect.center = (self.game.screen.get_width() // 2,
                       self.game.screen.get_height() // 2)
        pygame.draw.rect(self.game.screen, (50, 50, 80), rect)
