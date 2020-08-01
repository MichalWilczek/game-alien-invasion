import sys
import pygame


class AlienInvasion:
    """General class dedicated to managing the resources and the way the game works"""

    def __init__(self):
        """Game initialization and resources creation"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Alien invasion")

        # display color definition
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starting the main game loop"""
        while True:
            # waiting for a key or a mouse button to be pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # screen color refreshed at each loop iteration
            self.screen.fill(self.bg_color)

            # display of the last modified screen
            pygame.display.flip()


if __name__ == '__main__':
    # creating and starting the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
