import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class dedicated to manage the space ship"""

    def __init__(self, alien_invasion_game):
        """Initialization of the ship and its position"""
        super().__init__()

        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings
        self.screen_rect = alien_invasion_game.screen.get_rect()

        # load the spacecraft image and download its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # each new ship shows up at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # ship's position is stored as float
        self.x = float(self.rect.x)

        # options indicating the ship movement
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Spacecraft display in its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Placing the ship at the bottom center of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x.
        self.rect.x = self.x
