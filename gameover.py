class GameOver:
    def __init__(self, game):
        self.game = game

        self.restart_message = self._init_restart_message()

    def _init_restart_message(self):
        text = self.game.font.render(
            "Press R to restart or Q to quit", True, self.game.settings.font_colour
        )
        text_rect = text.get_rect()
        text_rect.center = (
            (self.game.rect.width // 2) + 400,
            self.game.rect.height // 2,
        )
        return [text, text_rect]

    def draw_restart(self, screen):
        text, rect = self.restart_message
        screen.blit(text, rect)

    def draw_winner(self, screen):
        winner_text = self._get_winner_text()

        text = self.game.font.render(winner_text, True, self.game.settings.font_colour)
        text_rect = text.get_rect()
        text_rect.center = (
            (self.game.rect.width // 2) + 100,
            self.game.rect.height // 2,
        )
        screen.blit(text, text_rect)

    def _get_winner_text(self):
        if self.game.winner == "No winner":
            winner_text = "No winners!"
        elif self.game.winner == "Push":
            winner_text = "Push, no winners!"
        elif self.game.winner == "Dealer":
            winner_text = "Dealer won!"
        elif self.game.winner == "Player":
            winner_text = "Player won!"

        return winner_text
