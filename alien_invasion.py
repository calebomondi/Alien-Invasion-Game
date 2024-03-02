import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf 
from alien import Alien
from button import Button

def run_game():
    #Initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    #Create a display window
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #Give the window a name 
    pygame.display.set_caption("Alien Invasion")
    #create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #Make a ship, a group of bullets(holds bullets) and a group of aliens(holds aliens)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    #create a fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #makke the play button
    play_button = Button(ai_settings,screen,"Play")

    while True:
        gf.check_events(ai_settings,screen,sb,ship,bullets,aliens,stats,play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,ship,screen,aliens,bullets,stats,play_button,sb)

run_game()