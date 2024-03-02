# A class to set all settings for for Alien invasion
class Settings():
    def __init__(self):
        """initialize game settings"""
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (255,255,255)
        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #how quickly the game speeds up
        self.speedup_scale = 1.1
        #how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction of 1 reps right; -1 reps left;
        self.fleet_direction = 1
        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and alien points values"""
        #speed
        self.ship_speed_factor *= self.speedup_scale 
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        #points
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)