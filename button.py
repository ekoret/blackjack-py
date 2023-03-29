import pygame


class Button:
    def __init__(self, game, text, left, top, width, height):
        self.game = game
        self.text = text
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        self.text = self.game.font.render(text, True, self.game.settings.font_colour)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.rect, 0, 4)
        screen.blit(self.text, self.text_rect)
