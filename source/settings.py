
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
