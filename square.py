import pygame


class Square:
    def __init__(self, x, y, size, colour, label_text, font_size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.label_text = label_text
        self.font_size = font_size

        self.bg_colour = (0, 0, 0)
        self.text_colour = (255, 255, 255)

        """Setup label"""
        self.font = pygame.font.SysFont('Arial', 20)
        self.label = self.font.render(
            self.label_text, True, self.text_colour, self.bg_colour)

        """Setup sqaure"""
        self.label_rect = self.label.get_rect()
        self.label_rect.center = (
            self.x + self.size // 2, self.y + self.size + self.label_rect.height // 2)

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour,
                         (self.x, self.y, self.size, self.size))
        surface.blit(self.label, self.label_rect)
