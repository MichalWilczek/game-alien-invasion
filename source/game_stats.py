
class GameStats:
    """Monitoring statistical data in the game"""

    def __init__(self, alien_invasion):
        """Statistical data initialization"""
        self.settings = alien_invasion.settings
        self.ships_left = None
        self.score = None
        self.level = None
        self.reset_stats()

        # starting the game in inactive mode
        self.game_active = False

        # the best score in game should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialization of the statistical data which can vary in the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
