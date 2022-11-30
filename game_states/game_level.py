import pygame, os
from game_states.game_state import State

class Game_Level(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.bg_sky = pygame.image.load(os.path.join(self.game.assets_Pointer, "level_assets", "Background.png")).convert()
        self.bg_sky = pygame.transform.scale(self.bg_sky, (500, 300))

    
    def update(self, delta_Time, user_Actions):
        pass

    def render(self, display):
        display.blit(self.bg_sky, (0,0))