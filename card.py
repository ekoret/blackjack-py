import pygame


class Card(pygame.sprite.Sprite):
    """
    TODO:
    - override update()

        Must contain:
        - Sprite.image attribute
        - Sprite.rect attribute
    """

    def __init__(self, value, suit):
        pygame.sprite.Sprite.__init__(self)

        self.value = value
        self.suit = suit.lower()
        self.is_showing = True

        self.image = pygame.image.load(f"images/cards/{value}_of_{suit}.bmp")
        self.rect = self.image.get_rect()

    def hide_card(self):
        self.is_showing = False
