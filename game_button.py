"""Module for creating buttons"""

import pygame


class GameButton:
    def __init__(self, x, y, width, height, text,
                 font_size=20,
                 font_name="Arial",
                 text_colour=(255, 255, 255),
                 bg_colour=(150, 150, 150),
                 bg_colour_hover=(170, 10, 200)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.bg_colour = bg_colour
        self.bg_colour_hover = bg_colour_hover
        self.text_colour = text_colour

        """Define font"""
        self.font = pygame.font.SysFont(font_name, self.font_size)

        """Create rect, set dimensions, set coordinates from center"""
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x + (self.width / 2),
                            self.y + (self.height / 2))

        """Create text, set styles, set coordinate from center of rect"""
        self.surface = self.font.render(self.text, True, self.text_colour)
        self.surface_rect = self.surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        """Handle mouse hover"""
        mouse_pos = pygame.mouse.get_pos()
        bg_colour = self.bg_colour
        if (self.rect.collidepoint(mouse_pos)):
            bg_colour = self.bg_colour_hover

        pygame.draw.rect(screen, bg_colour, self.rect)
        screen.blit(self.surface, self.surface_rect)

    def handle_events(self, event, game, current_player):
        """Event loop for button clicks"""
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if self.rect.collidepoint(event.pos):
                if (self.text.lower() == "hit"):
                    """Deal card to player"""
                    current_player.add_card(game.deck.deal_card())

                    """Increment player if 21 is hit"""
                    if (current_player.get_hand_total() == 21):
                        self.handle_turn_change(game)

                    """Handle bust"""
                    if (current_player.get_hand_total() > 21):
                        current_player.lost = True
                        self.handle_turn_change(game)

                if (self.text.lower() == "stay"):
                    self.handle_turn_change(game)

                if (game.game_over == True):
                    if (self.text.lower() == "reset"):
                        print("reset")

    def handle_turn_change(self, game):
        if (game.current_player_turn + 1 > len(game.players)):
            game.current_player_turn = 0
        else:
            game.current_player_turn += 1
