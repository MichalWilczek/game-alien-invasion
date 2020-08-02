import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class describing a single alien in the fleet"""

    def __init__(self, alien_invasion):
        """Alien initialization and its initial position definition"""

        super().__init__()
        self.screen = alien_invasion.screen

        # load the alien image and download its rectangle
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # alien positioning at top left side of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # alien's position is stored as float
        self.x = float(self.rect.x)
