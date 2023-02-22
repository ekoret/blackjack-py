import sys

import pygame


class PygameManager:

    def __init__(self):
        pygame.init()
        self.pygame_instance = pygame
        self.clock = pygame.time.Clock()  # framerate
        self.screen = self.get_screen((1200, 800))
        pygame.font.init()
        self.framerate = 30

    def update_screen(self):
        pygame.display.flip()  # draw the screen current screen

    def set_font_arial(self, size=20):
        pygame.font.SysFont('Arial', size)

    def set_window_title(self, title):
        pygame.display.set_caption(title)  # title of window

    def get_screen(self, screen_w_h):
        return pygame.display.set_mode((screen_w_h[0], screen_w_h[1]))

    def close(self):
        sys.exit()

    def tick(self, framerate=30):
        self.clock.tick(framerate)
