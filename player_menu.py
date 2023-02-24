import pygame


class PlayerMenu:
    def __init__(self, game):
        self.game = game
        self.height = 47
        self.bg_colour = (0, 0, 0)
        self.text_colour = (255, 255, 255)
        self.x_offset = 80
        self.y_offset = 200
        self.width = 225

    def draw(self, player):
        """Menu background"""
        rect_bg = pygame.Rect(player.x - 80, player.y - 200, 250, 200)
        pygame.draw.rect(self.game.screen, self.bg_colour, rect_bg)

        for i, move in enumerate(self.game.settings.moves):
            text_surface = self.game.font.render(
                move.upper(), True,  self.text_colour, (200, 50, 50))
            rect = pygame.Rect(player.x - self.x_offset, player.y - self.y_offset,
                               self.width, (i + 1) * self.height)

            x = rect.x + 10
            y = rect.y + (rect.height - text_surface.get_height()) // 2
            self.game.screen.blit(text_surface, (x, y))
