# Blackjack game file
import pygame
from icecream import ic

from settings import Settings
from deck import Deck
from player import Player, Dealer


class Blackjack:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(self)
        self.dealer = Dealer(self)
        self.deck = Deck(self)
        self.dealer.deal_game()

    def run_game(self):
        while self.running:
            self._check_events()

            self._draw_bg()

            # Render game here
            self.player.draw_cards(self.screen)
            self.dealer.draw_cards(self.screen)

            self._update_screen()

        self._quit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update_screen(self):
        pygame.display.flip()
        self.clock.tick(self.settings.framerate)  # limits FPS to 60

    def _draw_bg(self):
        self.screen.fill((33, 33, 33))

    def _quit(self):
        pygame.quit()


if __name__ == "__main__":
    blackjack = Blackjack()
    blackjack.run_game()
