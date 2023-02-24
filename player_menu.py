import pygame


class PlayerMenu:
    def draw(self, game, player):
        """Menu heading"""
        # text_surface = game.font.render("Menu", True, (255, 255, 255))

        """Manu background"""
        rect_bg = pygame.Rect(player.x - 80, player.y - 200, 250, 200)

        pygame.draw.rect(game.screen, (0, 0, 0), rect_bg)
        # game.screen.blit(text_surface, (player.x - 80, player.y - 210))
