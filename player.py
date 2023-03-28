import pygame


class Player:
    def __init__(self, game):
        self.game = game
        self.name = "John Doe"
        self.cards = pygame.sprite.Group()

    def add_card(self, card):
        self.cards.add(card)


class Dealer(Player):
    def __init__(self, game):
        super().__init__(game)
        self.name = "Dealer"

    def deal_game(self):
        players = [self.game.player, self.game.dealer]

        for _ in range(2):
            for player in players:
                card = self.game.deck.get_top_card()
                player.add_card(card)
