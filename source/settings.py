
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

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
