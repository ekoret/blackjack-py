import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.animation_cooldown = 250


class DealerSprite(Sprite):
    def __init__(self, x=1200 // 2 + 72, y=25):
        super().__init__(x, y)

        self.width = 72
        self.height = 172

        """
        TODO: Sprite sheet for Bernard needs to be fixed to be
              exact pixel dimensions for each frame
        """
        self.sheet = pygame.image.load(
            "images/sprite-sheets/bernard/alien-bernard-standing.png").convert_alpha()

        self.animations = {
            "standing": {
                "steps": 3,
                "current_frame": 0
            }
        }

    def draw(self, screen, frame):
        image = self.get_image(frame)
        screen.blit(image, (self.x, self.y))

    def get_image(self, frame, scale=1):
        image = pygame.Surface((self.width, self.height)).convert_alpha()
        image.blit(self.sheet, (0, 0),
                   ((frame * self.width), 0, self.width, self.height))
        # image = pygame.transform.scale(
        #     image, (self.width * scale, self.height * scale))
        image.set_colorkey((0, 0, 0))
        return image
