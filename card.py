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

        self.size = self.image.get_size()
        self.image = pygame.transform.scale(
            self.image, (int(self.size[0] // 1.5), int(self.size[1] // 1.5))
        )
        self.rect = self.image.get_rect()

    def hide_card(self):
        self.is_showing = False
