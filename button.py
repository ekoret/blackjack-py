import pygame


class Button:
    def __init__(self, game, text, left, top, width, height):
        self.game = game
        self.button_text = text
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self.default_colour = (100, 100, 100)
        self.hover_colour = (125, 125, 125)

        self.bg_colour = (100, 100, 100)

        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        self.text = self.game.font.render(
            self.button_text, True, self.game.settings.font_colour
        )
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_colour, self.rect, 0, 4)
        screen.blit(self.text, self.text_rect)

    def check_hover(self, event):
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            hit = self.rect.collidepoint(mouse_pos)
            if hit:
                self.bg_colour = self.hover_colour
            else:
                self.bg_colour = self.default_colour

    def check_click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(mouse_pos)

        if event.type == pygame.MOUSEBUTTONDOWN and hit:
            if self.button_text == "HIT":
                current_player = self.game.player_list[self.game.current_player_turn]
                self.game.player_moves.hit(current_player)

                if current_player.get_hand_total() == 21:
                    print("BLACKJACK")
                    self.game.current_player_turn += 1
                elif current_player.get_hand_total() > 21:
                    print("BUST")
                    self.game.current_player_turn += 1
