
class Settings:
    """Class dedicated to store all game settings"""

    def __init__(self):
        """Game settings initialization"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600

        # display color definition
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # change of game level
        self.speed_up_scale = 1.1
        self.initialize_dynamic_settings()

        # scores data
        self.alien_points = None
        # change of points with increasing game level
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Settings initialization which change as the game proceeds"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

        # scores data
        self.alien_points = 50

    def increase_speed(self):
        """Change of settings related to speed"""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale)
