import pygame


class Player:
    def __init__(self, game):
        self.game = game
        self.name = "John Doe"
        self.cards = pygame.sprite.Group()

        self.card_spacing = 125
        self.card_x_location = 600

    def add_card(self, card):
        self.cards.add(card)

    def _get_hand_total(self):
        total = 0
        for card in self.cards:
            value = card.value
            if value in ("jack", "queen", "king", "ace"):
                value = 10
            total += value
        return total

    def draw_hand_total(self, screen):
        y_offset = 310
        text = self.game.font.render(
            f"Total: {self._get_hand_total()}", True, self.game.settings.font_colour
        )
        screen.blit(text, (400, self.game.rect.height - y_offset))

    def draw_cards(self, screen):
        x_offset = 0
        y_offset = 200
        x_offset_increment = self.card_spacing
        for card in self.cards:
            card.rect.centerx = self.card_x_location + x_offset
            card.rect.centery = self.game.rect.height - y_offset

            x_offset += x_offset_increment
        self.cards.draw(screen)


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

    def draw_cards(self, screen):
        x_offset = 0
        x_offset_increment = self.card_spacing
        for card in self.cards:
            card.rect.centerx = self.card_x_location + x_offset
            card.rect.centery = 200

            x_offset += x_offset_increment
        self.cards.draw(screen)

    def draw_hand_total(self, screen):
        y_offset = 310
        text = self.game.font.render(
            f"Total: {self._get_hand_total()}", True, self.game.settings.font_colour
        )
        screen.blit(text, (400, y_offset))
