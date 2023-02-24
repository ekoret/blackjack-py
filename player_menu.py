from game_button import GameButton


class PlayerMenu:
    def __init__(self, game):
        self.game = game
        self.height = 200
        self.width = 250
        self.x_offset = 90
        self.y_offset = 200
        self.bg_colour = (0, 0, 0)
        self.text_colour = (255, 255, 255)

    def draw(self, player):
        self.x = player.x - self.x_offset
        self.y = player.y - self.y_offset
        button_list = self.get_button_list()
        self.button_list = button_list
        for button in self.button_list:
            button.draw(self.game.screen)

    """
    Creates buttons and sizes + sets coordinates 
    for them based on the amount of moves in the game settings
    and for the current player turn
    """

    def get_button_list(self):
        button_list = []

        button_height = (self.height // len(self.game.settings.moves))
        for i, move in enumerate(self.game.settings.moves):
            button = GameButton(
                self.x, self.y + (i * button_height), self.width, button_height, move, 20, "Arial", (255, 255, 255), (111, 111, 111), (150, 150, 150))
            button_list.append(button)
        return button_list
