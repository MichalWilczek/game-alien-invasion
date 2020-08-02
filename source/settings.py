
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
        self.ship_limit = 1

        # bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
