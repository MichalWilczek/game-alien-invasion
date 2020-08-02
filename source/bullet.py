import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class dedicated to manage bullets shot by the ship"""

    def __init__(self, alien_invasion_game):
        super().__init__()
        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings
        self.color = self.settings.bullet_color

        # creation of the bullet rectangle at position (0, 0)
        # then, its proper position definition
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = alien_invasion_game.ship.rect.midtop

        # bullet position defined with a float
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet on the screen"""
        # bullet position update
        self.y -= self.settings.bullet_speed
        # bullet rectangle update
        self.rect.y = self.y

    def draw_bullet(self):
        """Bullet display on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
