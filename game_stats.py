class GameStats():
    """Track statitics for Alien Invasion"""
    def __init__(self,ai_settings):
        #initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()
        #start alien invasion in an active state
        self.game_active = False
        #high score should never be reset
        self.high_score = 0
    
    def reset_stats(self):
        #initialize stats that can change during the game
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        