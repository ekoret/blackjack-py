import pygame

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
        self.buttons = [GameButton(100, 100, 200, 80, "HIT", 20, "Arial", (255, 255, 255), (15, 15, 15), (25, 25, 25)),
                        GameButton(100, 200, 200, 80, "STAY", 20, "Arial", (255, 255, 255), (15, 15, 15), (25, 25, 25))]

    def draw(self, player):
        for button in self.buttons:
            button.draw(self.game.screen)
