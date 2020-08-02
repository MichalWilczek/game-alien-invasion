import pygame.font
from pygame.sprite import Group
from source.ship import Ship


class Scoreboard:
    """Class for presenting scores"""

    def __init__(self, alien_invasion):
        """Initialization of attributes about scores"""
        self.alien_invasion = alien_invasion
        self.screen = alien_invasion.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = alien_invasion.settings
        self.stats = alien_invasion.stats

        # font settings for score data
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # initial picture with score data
        self.score_image = None
        self.score_rect = None
        self.prep_score()

        self.high_score_image = None
        self.high_score_rect = None
        self.prep_high_score()

        self.level_image = None
        self.level_rect = None
        self.prep_level()

        self.ships = None
        self.prep_ships()

    def prep_score(self):
        """Converts score data into a picture"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        # display of score data at top right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Converts the highest score into a picture"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)

        # showing the best score in the game at top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Converts the level number into a picture"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)

        # level number is shown under the current number of points
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Shows the amount of ships left during the game"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.alien_invasion)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Shows score data on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Checks whether the highest score was reached during the game"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
