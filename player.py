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

    def get_hand_total(self):
        total = 0
        for card in self.cards:
            value = card.value
            if value in ("jack", "queen", "king", "ace"):
                value = 10
            total += value
        return total

    def draw_stats(self, screen):
        y_offset = 310
        text = self.game.font.render(
            f"Total: {self.get_hand_total()}", True, self.game.settings.font_colour
        )
        screen.blit(text, (390, self.game.rect.height - y_offset))

        if self.get_hand_total() == 21:
            blackjack_text = self.game.font.render(
                "BLACKJACK", True, self.game.settings.font_colour
            )
            blackjack_text_rect = blackjack_text.get_rect()
            blackjack_text_rect.center = (
                self.game.rect.width // 2,
                self.game.rect.height - y_offset,
            )
            screen.blit(
                blackjack_text,
                blackjack_text_rect,
            )

        if self.get_hand_total() > 21:
            bust_text = self.game.font.render(
                "BUST", True, self.game.settings.font_colour
            )
            bust_text_rect = bust_text.get_rect()
            bust_text_rect.center = (
                self.game.rect.width // 2,
                self.game.rect.height - y_offset,
            )
            screen.blit(
                bust_text,
                bust_text_rect,
            )

    def draw_cards(self, screen):
        x_offset = 0
        y_offset = 200
        x_offset_increment = self.card_spacing
        for card in self.cards:
            card.rect.centerx = self.card_x_location + x_offset
            card.rect.centery = self.game.rect.height - y_offset

            x_offset += x_offset_increment
        self.cards.draw(screen)

    def draw(self, screen):
        self.draw_cards(screen)
        self.draw_stats(screen)


class Dealer(Player):
    def __init__(self, game):
        super().__init__(game)
        self.name = "Dealer"

    def deal_game(self):
        players = [self.game.player, self.game.dealer]

        for _ in range(2):
            for player in players:
                if len(players[1].cards) == 1 and len(players[0].cards) == 2:
                    break
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

    def draw_stats(self, screen):
        y_offset = 310
        hand_total_text = self.game.font.render(
            f"Total: {self.get_hand_total()}", True, self.game.settings.font_colour
        )
        screen.blit(hand_total_text, (390, y_offset))

        if self.get_hand_total() == 21:
            blackjack_text = self.game.font.render(
                "BLACKJACK", True, self.game.settings.font_colour
            )
            blackjack_text_rect = blackjack_text.get_rect()
            blackjack_text_rect.center = (self.game.rect.width // 2, y_offset)
            screen.blit(blackjack_text, blackjack_text_rect)

        if self.get_hand_total() > 21:
            bust_text = self.game.font.render(
                "BUST", True, self.game.settings.font_colour
            )
            bust_text_rect = bust_text.get_rect()
            bust_text_rect.center = (self.game.rect.width // 2, y_offset)
            screen.blit(bust_text, bust_text_rect)

    def play(self):
        while self.get_hand_total() < 16:
            card = self.game.deck.get_top_card()
            self.add_card(card)
        self.game.game_over = True
