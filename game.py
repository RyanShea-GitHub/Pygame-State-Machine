import os
import pygame
from pygame import *
import time

from game_states.splash_screen import Splash
from game_states.game_level import Game_Level

class Game():
        def __init__(self):
            pygame.init()

            self.pygame.title("Test State Machine")
            
            self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 500, 300
            self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 600
            self.game_canvas = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
            self.running, self.playing = True, True

            self.user_Actions = {"left": False, "Right": False, "Up": False, "Down": False,
            "Slide": False, "Jump": False, "Pause": False, "Roll": False, "Start": False}

            self.delta_Time, self.prev_Time = 0, 0

            self.state_Stack = []
            self.load_assets()
            self.load_States()


        def game_Loop(self):
            while self.playing:
                self.get_Player_Input()
                self.render()
                self.update()
                self.get_Time()


        def get_Player_Input(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running, self.playing = False, False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.user_Actions["Up"] = True
                    if event.key == pygame.K_s:
                        self.user_Actions["Down"] = True
                    if event.key == pygame.K_a:
                        self.user_Actions["Left"] = True
                    if event.key == pygame.K_d:
                        self.user_Actions["Right"] = True
                    if event.key == pygame.K_LSHIFT:
                        self.user_Actions["Slide"] = True
                    if event.key == pygame.K_ESCAPE:
                        self.user_Actions["Pause"] = True
                    if event.key == pygame.K_e:
                        self.user_Actions["Roll"] = True
                    if event.key == pygame.K_SPACE:
                        self.user_Actions["Jump"] = True
                    if event.key == pygame.K_RETURN:
                        self.user_Actions["Start"] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.user_Actions["Up"] = False
                    if event.key == pygame.K_s:
                        self.user_Actions["Down"] = False
                    if event.key == pygame.K_a:
                        self.user_Actions["Left"] = False
                    if event.key == pygame.K_d:
                        self.user_Actions["Right"] = False
                    if event.key == pygame.K_LSHIFT:
                        self.user_Actions["Slide"] = False
                    if event.key == pygame.K_ESCAPE:
                        self.user_Actions["Pause"] = False
                    if event.key == pygame.K_e:
                        self.user_Actions["Roll"] = False
                    if event.key == pygame.K_SPACE:
                        self.user_Actions["Jump"] = False
                    if event.key == pygame.K_RETURN:
                        self.user_Actions["Start"] = False
            
                    
        def render(self):
            self.state_Stack[-1].render(self.game_canvas)
            self.screen.blit(pygame.transform.scale(self.game_canvas, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0, 0))
            pygame.display.flip()

        def update(self):
            self.state_Stack[-1].update(self.delta_Time, self.user_Actions)

        def get_Time(self):
            current_Time = time.time()
            self.delta_Time = current_Time - self.prev_Time
            self.prev_Time = current_Time

        def load_assets(self):
            self.assets_Pointer =  os.path.join("assets")
            self.level_Pointer = os.path.join(self.assets_Pointer, "level_assets")
            self.sprite_Pointer = os.path.join(self.assets_Pointer, "sprites")
            self.font_Pointer = os.path.join(self.assets_Pointer, "font")
            self.font = pygame.font.Font(os.path.join(self.font_Pointer, "Galaxy_dingbats.ttf"), 30)

        def load_States(self):
            self.splash_sc = Splash(self)
            self.state_Stack.append(self.splash_sc)

        def draw_Text(self, surface, text, colour, x, y):
            text_Surface = self.font.render(text, True, colour)
            text_Box = text_Surface.get_rect()
            text_Box.center = (x, y)
            surface.blit(text_Surface, text_Box)

        def reset_keys(self):
            for action in self.user_Actions:
                self.user_Actions[action] = False

if __name__ == "__main__":
    game_Instance = Game()
    while game_Instance.running:
        game_Instance.game_Loop()