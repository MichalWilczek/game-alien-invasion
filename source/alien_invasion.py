import sys
import pygame
from source.settings import Settings
from source.ship import Ship


class AlienInvasion:
    """General class dedicated to managing the resources and the way the game works"""

    def __init__(self):
        """Game initialization and resources creation"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Starting the main game loop"""
        while True:
            # waiting for a key or a mouse button to be pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # screen color refreshed at each loop iteration
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # display of the last modified screen
            pygame.display.flip()


if __name__ == '__main__':
    # creating and starting the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
