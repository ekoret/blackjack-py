from game_button import GameButton


class PlayerMenu:
    def __init__(self, game):
        self.game = game
        self.height = 200
        self.width = 250
        self.x_offset = 60
        self.y_offset = 100
        self.bg_colour = (0, 0, 0)
        self.text_colour = (255, 255, 255)

    def draw(self, player):
        for i, move in enumerate(self.game.settings.moves):
            button = GameButton(player.x - self.x_offset, (player.y - (100 * i)) - 100,
                                200, 80, move, 20, "Arial", (255, 255, 255), (15, 15, 15), (25, 25, 25))
            button.draw(self.game.screen)
