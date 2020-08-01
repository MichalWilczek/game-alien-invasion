import pygame


class Ship:
    """Class dedicated to manage the space ship"""

    def __init__(self, alien_invasion_game):
        """Initialization of the ship and its position"""

        self.screen = alien_invasion_game.screen
        self.screen_rect = alien_invasion_game.screen.get_rect()

        # load the spacecraft image and download its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # each new ship shows up at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Spacecraft display in its current position"""
        self.screen.blit(self.image, self.rect)
