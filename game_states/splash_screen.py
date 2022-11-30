from game_states.game_state import State
from game_states.game_level import Game_Level

class Splash(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, delta_Time, user_Actions):
        if user_Actions["Start"]:
            new_State = Game_Level(self.game)
            new_State.enter_State()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_Text(display, "DEMO TEXT", (0,0,0), self.game.DISPLAY_WIDTH/2, self.game.DISPLAY_HEIGHT/2)