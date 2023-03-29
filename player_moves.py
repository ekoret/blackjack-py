import pygame

from button import Button


class PlayerMoves:
    def __init__(self, game):
        self.game = game
        self.x_pos = 325
        self.y_pos = 440

        self.container_rect = pygame.Rect(self.x_pos, self.y_pos, 200, 150)
        self.buttons = self._init_buttons()

    def _init_buttons(self):
        player_moves = ("HIT", "PASS")
        y_offset = 0
        buttons = []
        for move in player_moves:
            button = Button(
                self.game,
                move,
                self.container_rect.left + 20,
                self.container_rect.top + 20 + y_offset,
                self.container_rect.width - 40,
                50,
            )
            buttons.append(button)
            y_offset += 60
        return buttons

    def draw(self, screen):
        # container to wrap buttons
        pygame.draw.rect(screen, (77, 77, 77), self.container_rect, 0, 4)

        # buttons
        for button in self.buttons:
            button.draw(screen)
