import pygame


class PlayerMenu:
    def draw(self, game, player):
        """Menu heading"""
        text_surface = game.font.render(
            "Menu", True, (255, 255, 255))

        """Manu background"""
        rect_bg = pygame.Rect(100, 100, 300, 400)

        pygame.draw.rect(game.screen, (170, 40, 170), rect_bg)
        game.screen.blit(text_surface, (100, 300))
