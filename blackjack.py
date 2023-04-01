# Blackjack game file
import pygame
from icecream import ic

from settings import Settings
from deck import Deck
from player import Player, Dealer
from player_moves import PlayerMoves
from gameover import GameOver


class Blackjack:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.settings = Settings()
        self.font = pygame.font.SysFont("Arial Black", 16)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False

        self.player = Player(self)
        self.dealer = Dealer(self)
        self.deck = Deck(self)
        self.dealer.deal_game()

        self.player_moves = PlayerMoves(self)

        self.player_list = [self.player, self.dealer]
        self.current_player_turn = 0
        self.winner = None

        self.game_over_screen = GameOver(self)

    def run_game(self):
        while self.running:
            self._check_events()

            self._draw_bg()
            # Render game here
            self.player.draw(self.screen)
            self.player_moves.draw(self.screen)

            self.dealer.draw(self.screen)

            if self.current_player_turn == len(self.player_list) - 1:
                self.dealer.play()

                player_hand_total = self.player.get_hand_total()
                dealer_hand_total = self.dealer.get_hand_total()

                if player_hand_total > 21 and dealer_hand_total > 21:
                    self.winner = "No winner"
                elif (player_hand_total < 22 and dealer_hand_total > 21) or (
                    player_hand_total < 22
                    and dealer_hand_total < 22
                    and player_hand_total > dealer_hand_total
                ):
                    self.winner = "Player"
                elif (player_hand_total > 21 and dealer_hand_total < 22) or (
                    player_hand_total < 22
                    and dealer_hand_total < 22
                    and player_hand_total < dealer_hand_total
                ):
                    self.winner = "Dealer"
                elif player_hand_total == dealer_hand_total:
                    self.winner = "Push"

                self.game_over = True

            if self.game_over:
                self.game_over_screen.draw_winner(self.screen)
                self.game_over_screen.draw_restart(self.screen)

            self._update_screen()

        self._quit()

    def change_turn(self):
        self.current_player_turn += 1

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                if event.key == pygame.K_r:
                    self._restart()

            # Check player move button events
            for button in self.player_moves.buttons:
                button.check_hover(event)
                button.check_click(event)

    def _restart(self):
        self.current_player_turn = 0
        self.game_over = False
        self.player = Player(self)
        self.dealer = Dealer(self)
        self.player_list = [self.player, self.dealer]
        self.deck = Deck(self)
        self.winner = None
        self.dealer.deal_game()

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
