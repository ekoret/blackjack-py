# Blackjack game file
import pygame

from settings import Settings


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

    def run_game(self):
        while self.running:
            self._check_events()

            self._draw_bg()

            # Render game here

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
        self.screen.fill("purple")

    def _quit(self):
        pygame.quit()


if __name__ == "__main__":
    blackjack = Blackjack()
    blackjack.run_game()
