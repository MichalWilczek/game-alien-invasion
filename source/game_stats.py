
class GameStats:
    """Monitoring statistical data in the game"""

    def __init__(self, alien_invasion):
        """Statistical data initialization"""
        self.settings = alien_invasion.settings
        self.ships_left = None
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialization of the statistical data which can vary in the game"""
        self.ships_left = self.settings.ship_limit
